export type RegisterFunction = (id: string) => DialogsContainer
export type ElementLike = JSX.Element | string | ElementLike[]

export interface DialogsContainer {
  unmount(): boolean
  open(id: string, element: ElementLike): void
  close(id: string): boolean
}
