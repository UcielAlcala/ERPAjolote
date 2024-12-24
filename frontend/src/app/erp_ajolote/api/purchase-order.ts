import { Supplier } from './supplier';
import { Material } from './material';

export interface PurchaseOrder {
    id?: number;
    supplier: Supplier;
    order_date: Date;
    expected_date: Date;
    status: 'Pending' | 'Approved' | 'Received' | 'Closed' | 'Canceled';
    total_cost: number;
    created_at: Date;
    updated_at: Date;
    items: PurchaseOrderItem[];
}

export interface PurchaseOrderItem {
    id?: number;
    purchase_order: number; // This should be the ID of the PurchaseOrder
    material: Material;
    quantity: number;
    cost_per_unit: number;
    total_cost: number;
    received_quantity: number;
    created_at?: Date;
    updated_at?: Date;
}

