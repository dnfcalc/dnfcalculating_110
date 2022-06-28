import { useDialog } from "@/components/hooks/dialog"
import axios, { AxiosInstance, AxiosResponse } from "axios"
import { useConfigStore } from "@/store"
import { h } from "vue"

export interface HttpResponse<T = unknown> {
  code?: number
  message: string
  data: T
  state?: number
}

let instance: AxiosInstance | null = null

const baseURL = "http://127.0.0.1:17173/api"

export function defineRequest<T>(fn: (ax: AxiosInstance) => T) {
  if (!instance) {
    instance = axios.create({
      baseURL
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
      async (response: AxiosResponse<HttpResponse>) => {
        if (response.data.code === 500) {
          const { alert } = useDialog()
          await alert({
            content: () => {
              return h("div", { class: "justify-center text-hex-d4d6b6 text-center", style: "white-space:pre-wrap;width:250px" }, response.data.message)
            }
          })
        }
        return response.data
      },
      async (error: Error) => {
        return Promise.reject(error)
      }
    )
  }

  return fn(Object.create(instance))
}
