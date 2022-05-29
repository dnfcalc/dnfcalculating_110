import { ElementLike } from "./types"
import { onMounted, provide, reactive, renderList } from "vue"
import { REGISTER_DILOAG } from "./constants"

export type DialogInstance = {
  readonly id: string
  show: boolean
  cache: boolean
  render: () => JSX.Element
}

export function useContainer() {
  const dialogs = reactive(new Map<string, Map<string, ElementLike>>())

  //注册窗口
  function register(id: string) {
    dialogs.set(id, new Map())
    return {
      unmount() {
        return dialogs.delete(id)
      },
      open(did: string, element: ElementLike) {
        const container = dialogs.get(id)
        if (container) {
          container.set(did, element)
        }
      },
      close(did: string) {
        const container = dialogs.get(id)
        if (container) {
          return container.delete(did)
        }
        return false
      }
    }
  }

  provide(REGISTER_DILOAG, register)

  onMounted(() => {
    dialogs.clear()
  })

  function render() {
    return renderList(Array.from(dialogs.values()), e => Array.from(e.values()))
  }

  return { render }
}
