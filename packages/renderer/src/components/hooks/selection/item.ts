import { computed, ComputedRef, inject, onDeactivated, PropType, Ref, renderSlot } from "vue"
import { defineHooks } from "../define"
import { AciveClassSymbol, AciveSymbol, InitSymbol, ItemClassSymbol, Option, UnactiveSymbol } from "./constants"
import { BaseType, ClassType, valuePropType } from "../types"

export const itemProps = {
  value: {
    type: valuePropType,
    required: true
  },
  label: {
    type: [Function, String] as PropType<string | ((val: BaseType) => string) | null>,
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
  const active = inject(AciveSymbol) as Ref<Option>
  const init = inject<(obj: any) => () => void>(InitSymbol)

  const isActive = computed<boolean>(() => {
    return props.value == active?.value?.value
  })

  function render() {
    let label = props.label
    if (label) {
      if (typeof label == "function") {
        label = label(props.value)
      }
    }
    return label ?? renderSlot(slots, "default")
  }

  const id = Math.random().toString(36).slice(2, 9)

  const current = computed(() => {
    return {
      id,
      render,
      value: props.value
    }
  })

  if (!!init) {
    const remove = init(current)

    onDeactivated(remove)
  }

  function change() {
    if (!!active) {
      active.value = current.value
    }
  }

  const itemClass = computed(() => {
    return [inject<ComputedRef<ClassType>>(ItemClassSymbol)?.value ?? ""].concat(isActive.value ? activeClass.value : unactiveClass.value)
  })

  const activeClass = computed(() => {
    return inject<ComputedRef<ClassType>>(AciveClassSymbol)?.value ?? "active"
  })

  const unactiveClass = computed(() => {
    return inject<ComputedRef<ClassType>>(UnactiveSymbol)?.value ?? "unactive"
  })

  return {
    change,
    render,
    active,
    isActive,
    current,
    activeClass,
    unactiveClass,
    itemClass
  }
})

export interface ItemProps {}
