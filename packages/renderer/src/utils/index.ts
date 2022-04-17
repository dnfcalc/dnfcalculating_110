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

export function mapWithKeys<T extends object>(obj: T, keys?: (keyof T)[]) {
    if (!keys) {
        keys = Object.keys(obj) as (keyof T)[]
    }
    return keys.map(e => {
        return {
            [e]: obj[e]
        } as T
    })
}

export function mapWithCount<T>(start: number, end: number, callback: (i: number) => T) {
    const array: T[] = []
    for (let i = start; i < end; i++) {
        array.push(callback(i))
    }
    return array
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
