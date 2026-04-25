export const W = 800;
export const H = 500;
export const LEVEL_W = 5400;
export const GROUND_Y = 460;

export const C = {
  gold:        0xF5A623,
  goldDark:    0xD4881A,
  goldLight:   0xFFD166,
  purple:      0x7B2FBE,
  purpleDark:  0x3D0E6E,
  purpleLight: 0xB567FF,
  pink:        0xFF5BA3,
  pinkDark:    0xCC3377,
  bg:          0x0A001A,
  white:       0xFFFFFF,
  black:       0x000000,
  gray:        0x888888,
  sky:         0x1A0840,
  skyMid:      0x2D1069,
};

export const SPEED         = 220;
export const JUMP_VEL      = -420;
export const DOUBLE_JUMP   = -340;
export const GRAVITY       = 700;
export const BULLET_SPEED  = 300;
export const SHOOT_COOLDOWN = 500;

export const PLATFORMS: { x: number; y: number; w: number }[] = [
  { x: 220,  y: 380, w: 120 },
  { x: 420,  y: 330, w: 100 },
  { x: 600,  y: 290, w: 100 },
  { x: 780,  y: 350, w: 120 },
  { x: 960,  y: 280, w: 90  },
  { x: 1120, y: 340, w: 110 },
  { x: 1320, y: 290, w: 100 },
  // gap zone ~1480-1570
  { x: 1600, y: 400, w: 130 },
  { x: 1780, y: 340, w: 100 },
  { x: 1950, y: 290, w: 90  },
  { x: 2120, y: 350, w: 120 },
  { x: 2320, y: 300, w: 100 },
  { x: 2500, y: 260, w: 90  },
  { x: 2680, y: 320, w: 110 },
  { x: 2880, y: 280, w: 100 },
  { x: 3060, y: 350, w: 120 },
  { x: 3260, y: 290, w: 100 },
  { x: 3450, y: 240, w: 90  },
  { x: 3640, y: 310, w: 110 },
  { x: 3840, y: 370, w: 120 },
  { x: 4020, y: 300, w: 100 },
  { x: 4220, y: 260, w: 90  },
  { x: 4420, y: 330, w: 120 },
  { x: 4640, y: 280, w: 100 },
  { x: 4840, y: 350, w: 120 },
];

export const NOTE_POSITIONS: { x: number; y: number }[] = [
  // Ground notes
  { x: 150,  y: 430 }, { x: 350,  y: 430 }, { x: 550,  y: 430 },
  { x: 750,  y: 430 }, { x: 1000, y: 430 }, { x: 1250, y: 430 },
  // Platform notes
  { x: 260,  y: 350 }, { x: 460,  y: 300 }, { x: 640,  y: 260 },
  { x: 820,  y: 320 }, { x: 1000, y: 250 }, { x: 1360, y: 260 },
  { x: 1640, y: 370 }, { x: 1820, y: 310 }, { x: 1990, y: 260 },
  { x: 2160, y: 320 }, { x: 2360, y: 270 }, { x: 2540, y: 230 },
  { x: 2720, y: 290 }, { x: 2920, y: 250 }, { x: 3100, y: 320 },
  { x: 3300, y: 260 }, { x: 3490, y: 210 }, { x: 3680, y: 280 },
  { x: 3880, y: 340 }, { x: 4060, y: 270 }, { x: 4260, y: 230 },
  { x: 4460, y: 300 }, { x: 4680, y: 250 }, { x: 4880, y: 320 },
  // Bonus cluster near end
  { x: 5000, y: 430 }, { x: 5050, y: 430 }, { x: 5100, y: 430 },
];

export const ENEMY_POSITIONS: { x: number; y: number; range: number }[] = [
  { x: 430,  y: 430, range: 150 },
  { x: 800,  y: 430, range: 140 },
  { x: 1140, y: 310, range: 90  },
  { x: 1620, y: 370, range: 100 },
  { x: 2140, y: 320, range: 100 },
  { x: 2700, y: 290, range: 90  },
  { x: 2900, y: 430, range: 160 },
  { x: 3280, y: 260, range: 90  },
  { x: 3660, y: 280, range: 90  },
  { x: 3870, y: 430, range: 140 },
  { x: 4240, y: 230, range: 80  },
  { x: 4470, y: 300, range: 100 },
  { x: 4870, y: 430, range: 130 },
];

export const EXTRA_LIVES: { x: number; y: number }[] = [
  { x: 650,  y: 255 },
  { x: 1680, y: 305 },
  { x: 2520, y: 225 },
  { x: 3460, y: 205 },
  { x: 4660, y: 245 },
];
