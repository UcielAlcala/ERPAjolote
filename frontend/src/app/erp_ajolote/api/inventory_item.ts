import { Warehouse } from './warehouse'

export interface InventoryItem {
  id: number;
  inventory: Warehouse;
  itemType: string;         // 'Material', 'PrintedPiece', 'FinalProduct'
  itemId: number;
  quantity: number;
  unit: string;
  createdAt: Date;
  updatedAt: Date;
}
