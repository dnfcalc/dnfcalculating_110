export interface TreeNode {
    label: string
    id?: string | number
    value?: any
    children?: TreeNode[]
    [key: string]: any
}

export interface TreeData {}
