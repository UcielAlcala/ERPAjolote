import { Material } from './material';

export interface PrintedPiece {
  id?: number;
  sku?: string;
  name: string;
  print_time: string;        // ISO 8601 duration string
  cost?: number;             // costo de la pieza impresa
  materials?: PrintedPieceMaterial[];  // relación con PrintedPieceMaterial
  image?: string;
  createdAt?: Date;
  updatedAt?: Date;
}


export interface PrintedPieceMaterial {
  id?: number;
  printed_piece?: number;    // Aquí se usará el ID de PrintedPiece
  material?: number;         // Aquí se usará el ID de Material
  quantity?: number;
  unit?: 'g' | 'kg';         // restringido a 'g' o 'kg'
  createdAt?: Date;
  updatedAt?: Date;
}
