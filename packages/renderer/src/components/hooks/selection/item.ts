import { computed, inject, onDeactivated, PropType, renderSlot } from "vue"
import { defineHooks } from "../define"
import { ElementLike } from "../dialog"
import { BaseType, valuePropType } from "../types"
import { AciveClassSymbol, ChangeActiveSymbol, InitSymbol, IsActiveSymbol, ItemClassSymbol, ItemLabelSymbol, UnactiveSymbol } from "./constants"

export const itemProps = {
  value: {
    type: valuePropType,
    default() {
      return Math.random().toString(16).slice(2)
    }
  },
  label: {
    type: [Function, String] as PropType<string | ((val: BaseType) => string) | ElementLike | null>,
    default: () => null
  },
  keepAlive: {
    type: Boolean,
    default: () => true
  },
  key: {
    type: [String, Number, Symbol] as PropType<string | number | symbol>,
    default: () => null
  }
}

export const useSelectionItem = defineHooks(itemProps, (props, { slots }) => {
  const init = inject(InitSymbol)

  const parentLabel = inject(ItemLabelSymbol)

  function render() {
    return renderSlot(slots, "default", {}, () => {
      let label = props.label ?? parentLabel
      if (label) {
        if (typeof label == "function") {
          label = label(props.value)!
        }
      }
      if (label) {
        return [label]
      }
      return []
    })
  }

  if (!!init) {
    const remove = init({
      id: Math.random().toString(16).slice(2),
      label: typeof props.label == "string" ? props.label : undefined,
      value: props.value,
      render
    })
    onDeactivated(remove)
  }

  let isActive = inject(IsActiveSymbol, (_: BaseType) => false)

  const changeActive = inject(ChangeActiveSymbol, (_: BaseType) => false)

  const itemClass = computed(() => {
    return [inject(ItemClassSymbol)?.value ?? ""].concat(isActive(props.value) ? activeClass.value : unactiveClass.value)
  })

  const activeClass = computed(() => inject(AciveClassSymbol)?.value ?? "active")
  const unactiveClass = computed(() => inject(UnactiveSymbol)?.value ?? "unactive")

  return {
    change() {
      changeActive(props.value)
    },
    render,
    isActive,
    activeClass,
    unactiveClass,
    itemClass
  }
})

export interface ItemProps {}
