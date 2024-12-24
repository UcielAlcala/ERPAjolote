export interface Order {
  id: number;
  user?: any;
  status: string;           // 'Pending', 'Completed'
  createdAt: Date;
  updatedAt: Date;
}
