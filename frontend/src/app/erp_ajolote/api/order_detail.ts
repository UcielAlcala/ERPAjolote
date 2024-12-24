import { OrderItem } from './order_item';
import { PrintedPiece } from './printed_piece';

export interface OrderDetail {
  id: number;
  orderItem: OrderItem;
  printedPiece: PrintedPiece;
  requiredQuantity: number;
  availableQuantity: number;
  materialNeeded: number;
  printTimeNeeded: string;  // ISO 8601 duration string
  cost: number;             // costo del detalle del pedido
  createdAt: Date;
  updatedAt: Date;
}
