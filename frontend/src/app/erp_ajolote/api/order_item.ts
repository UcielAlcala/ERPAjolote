import { Order } from './order';
import { FinalProduct } from './final_product';

export interface OrderItem {
  id: number;
  order: Order;
  finalProduct: FinalProduct;
  quantity: number;
  totalCost: number;        // costo total del producto en la orden
  createdAt: Date;
  updatedAt: Date;
}
