export interface Material {
    id?: number;
    sku?: string;
    name: string;
    type: string;       // e.g., Producción, Empaque, Envío
    sub_type: string;    // e.g., Filamento, Pegamento, etc.
    brand: string;
    color: string;
    unit: string;       // e.g., g, ml, m, unidades
    cost_per_unit: number;
    image?: File;
    description: string;
    createdAt?: Date;
    updatedAt?: Date;
  }
  