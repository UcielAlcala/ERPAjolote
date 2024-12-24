export interface FinalProduct {
    id?: number;
    sku?: string;
    name: string;
    description: string;
    total_cost?: number;        // costo total del producto final
    bom?: BOM[];
    image?: string;
    createdAt?: Date;
    updatedAt?: Date;
  }

export interface BOM {
  id?: number;
  final_product?: number;
  content_type: number;
  object_id: number;
  quantity: number;
  cost?: number;
  createdAt?: Date;
  updatedAt?: Date;

}
  