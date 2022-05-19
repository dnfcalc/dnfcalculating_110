/**
 * @Author: Kritsu
 * @Date:   2021/11/12 14:50:00
 * @Last Modified by:   Kritsu
 * @Last Modified time: 2021/11/17 18:41:46
 */
export function in_range(num: number, start: number, end: number) {
  return start <= num && num <= end
}

export function to_percent(num?: number, defaultValue: number = 0, suffix = "") {
  num = num ?? defaultValue
  return num?.multiply(100).round(2).toString().concat(suffix)
}

export function get_num(num?: number, defaultValue: number = 0) {
  return num ?? defaultValue
}

export function format_string(str: string, params: any = {}, ...args: any[]) {
  let num = 0
  str = str.replace(/{}/g, match => {
    return args[num++] ?? match
  })
  str = str.replace(/{\d+}/g, match => {
    const i = parseInt(match.slice(1, -1))
    return args[i] ?? match
  })
  str = str.replace(/{\w+}/g, match => {
    const name = match.slice(1, -1)
    return params[name] ?? match
  })
  return str
}

export function getFloat(value: any, n: any) {
  value = Number(value)
  n = n ? parseInt(n) : 0
  if (n <= 0) {
    return Math.round(value)
  }
  value = Math.round(value * Math.pow(10, n)) / Math.pow(10, n)
  value = Number(value).toFixed(n)
  return value
}

export function cartesian<T = any>(...arr: T[][]): T[][] {
  if (arr.length < 2) {
    return arr
  }
  return arr.reduce(
    (a, b) => {
      const ret: T[][] = []
      a.forEach(a => {
        b.forEach(b => {
          ret.push(a.concat([b]))
        })
      })
      return ret
    },
    [[]] as T[][]
  )
}

export function groupBy<T, K>(array: T[], callback: (t: T) => K, sortBy?: () => void) {
  const map = new Map<K, T[]>()
  for (let i = 0; i < array.length; i++) {
    const t = array[i]
    const key = callback(t)
    let temp: T[] = map.get(key) || []
    if (!map.has(key)) {
      map.set(key, temp)
    }
    temp.push(t)
  }

  return Array.from(map.values())
}

export function debounce_last(func: Function, wait: number) {
  let timer = NaN
  return function () {
    if (!!timer) {
      clearTimeout(timer)
    }
    timer = setTimeout(func, wait)
  }
}

export function format_float(f: number, digit: number = 2) {
  let m = Math.pow(10, digit)
  //@ts-ignore
  return Math.round(f * m, 10) / m
}

export function mapRecord<T extends keyof any, K>(status: Record<T, K>, callback: (value: K, key: T) => K) {
  const new_status = {} as Record<T, K>
  for (let key in status) {
    const value = callback(status[key], key)
    if (value) {
      new_status[key] = value
    }
  }
  return new_status
}

Array.prototype.max = function <T>(callback: (t: T) => number): [number, T | undefined] {
  let rs: [number, T | undefined] = [-1, undefined]
  let max = -1
  for (let i = 0; i < this.length; i++) {
    const item = this.at(i) as T
    const count = callback(item)
    if (count > max) {
      max = count
      rs = [i, item]
    }
  }
  return rs
}

Array.prototype.min = function <T>(callback: (t: T) => number): [number, T | undefined] {
  let rs: [number, T | undefined] = [-1, undefined]
  let min = -1
  for (let i = 0; i < this.length; i++) {
    const item = this.at(i) as T
    const count = callback(item)
    if (count < min) {
      min = count
      rs = [i, item]
    }
  }
  return rs
}

export function toObj(data: Object) {
  let temp = {}
  for (let key in data) {
    try {
      Object.defineProperty(temp, key, {
        value: RecordToObj(data[key]),
        writable: true,
        enumerable: true,
        configurable: true
      })
    } catch {
      Object.defineProperty(temp, key, {
        value: data[key],
        writable: true,
        enumerable: true,
        configurable: true
      })
    }
  }
  return temp
}

export function toMap(data: Object) {
  let temp = {}
  for (let key in data) {
    if (typeof data[key] === "object" && data[key].constructor != Array) {
      // 需要转换部分,不能是Array,也会被转换
      let sub = {}
      for (let subkey in data[key]) {
        Object.defineProperty(sub, subkey, {
          value: new Map(Object.entries(data[key][subkey])),
          writable: true,
          enumerable: true,
          configurable: true
        })
      }
      Object.defineProperty(temp, key, {
        value: sub,
        writable: true,
        enumerable: true,
        configurable: true
      })
    } else {
      Object.defineProperty(temp, key, {
        value: data[key],
        writable: true,
        enumerable: true,
        configurable: true
      })
    }
  }
  return temp
}


export function RecordToObj(todo: Record<string, Map<any, any>>) {
  let temp = {}
  for (let key in todo) {
    Object.defineProperty(temp, key, {
      value: Object.fromEntries(todo[key]),
      writable: true,
      enumerable: true,
      configurable: true
    })
  }
  return temp
}

export function getUuid() {
  if (typeof crypto === "object") {
    if (typeof crypto.randomUUID === "function") {
      return crypto.randomUUID()
    }
    if (typeof crypto.getRandomValues === "function" && typeof Uint8Array === "function") {
      const callback = (c: any) => {
        const num = Number(c)
        return (num ^ (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (num / 4)))).toString(16)
      }
      return "10000000-1000-4000-8000-100000000000".replace(/[018]/g, callback)
    }
  }
  let timestamp = new Date().getTime()
  let perforNow = (typeof performance !== "undefined" && performance.now && performance.now() * 1000) || 0
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, c => {
    let random = Math.random() * 16
    if (timestamp > 0) {
      random = (timestamp + random) % 16 | 0
      timestamp = Math.floor(timestamp / 16)
    } else {
      random = (perforNow + random) % 16 | 0
      perforNow = Math.floor(perforNow / 16)
    }
    return (c === "x" ? random : (random & 0x3) | 0x8).toString(16)
  })
}

export async function getSession(key: string) {
  let temp = {}
  if (window.ipcRenderer) {
    await window.ipcRenderer.invoke("getStorage", key).then(res => (temp = res))
  } else {
    temp = JSON.parse(sessionStorage.getItem(key) ?? "")
  }
  return temp
}

export function setSession(key: string, value: any) {
  if (window.ipcRenderer) {
    window.ipcRenderer.invoke("setStorage", {
      key: key,
      value: value
    })
  } else {
    sessionStorage.setItem(key, JSON.stringify(value))
  }
}
