import axios, { AxiosInstance, AxiosResponse } from "axios"
import { useConfigStore } from "@/store"

export interface HttpResponse<T = unknown> {
  code?: number
  message: string
  data: T
  state?: number
}

let instance: AxiosInstance

function getBaseUrl() {
  if (process.env.NODE_ENV === "development") {
    return "http://127.0.0.1:17173/api"
  } else if (process.env.NODE_ENV === "production") {
    return "http://127.0.0.1:17173/api"
  } else {
    return "http://127.0.0.1:17173/api"
  }
}

export function defineRequest<T>(fn: (ax: AxiosInstance) => T) {
  if (!instance) {
    instance = axios.create({
      baseURL: getBaseUrl()
    })

    instance.interceptors.request.use(
      request => {
        const configStore = useConfigStore()
        const token = configStore.token
        if (token) {
          if (request.headers) {
            request.headers["Access-Token"] = token
          }
        }
        return request
      },
      error => {
        // do something
        return Promise.reject(error)
      }
    )

    instance.defaults.headers.post["Content-Type"] = "application/json;charset=UTF-8"
    // add response interceptors
    instance.interceptors.response.use(
      (response: AxiosResponse<HttpResponse>) => {
        return response.data
      },
      error => {
        return Promise.reject(error)
      }
    )
  }

  return fn(Object.create(instance))
}
