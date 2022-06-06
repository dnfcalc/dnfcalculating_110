export {}

declare global {
  type Num = string | number

  type ID = Num
  interface Window {
    // Expose some Api through preload script
    ipcRenderer: import("electron").IpcRenderer
    removeLoading: () => void
  }

  interface Number {
    plus(value: number): number

    minus(value: number): number

    multiply(value: number): number

    divide(value: number): number

    perMulti(value: number): number

    round(digit?: number): number

    floor(digit?: number): number

    exactlyDivide(value: number): number
  }

  interface Array<T> {
    min(callback: (t: T) => number): [number, T | undefined]
    max(callback: (t: T) => number): [number, T | undefined]
  }

  const APP_VERSION: string
}
