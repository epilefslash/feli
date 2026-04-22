import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const { cv, puesto, idioma } = await req.json();

    if (!cv || !puesto) {
      return NextResponse.json({ error: "Faltan datos" }, { status: 400 });
    }

    const appUrl = process.env.NEXT_PUBLIC_APP_URL || "http://localhost:3000";

    // Guardamos los datos temporalmente en base64 para pasarlos por URL
    const datosEncoded = Buffer.from(JSON.stringify({ cv, puesto, idioma })).toString("base64url");

    const body = {
      items: [
        {
          title: "ResumeIA - CV Profesional",
          description: "3 versiones de CV + Cover Letter + Tips de entrevista",
          quantity: 1,
          unit_price: 7,
          currency_id: "USD",
        },
      ],
      back_urls: {
        success: `${appUrl}/resultados?datos=${datosEncoded}`,
        failure: `${appUrl}/mejorar?error=pago_fallido`,
        pending: `${appUrl}/mejorar?error=pago_pendiente`,
      },
      auto_return: "approved",
      locale: "es-AR",
    };

    const response = await fetch("https://api.mercadopago.com/checkout/preferences", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${process.env.MP_ACCESS_TOKEN}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    const data = await response.json();

    if (!response.ok) {
      console.error("Error MP:", data);
      return NextResponse.json({ error: "Error creando el pago" }, { status: 500 });
    }

    return NextResponse.json({ init_point: data.init_point });
  } catch (error) {
    console.error("Error crear-pago:", error);
    return NextResponse.json({ error: "Error interno" }, { status: 500 });
  }
}
