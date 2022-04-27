import { BaseType, classPropType, valuePropType } from "../types"
import { computed, PropType, provide, reactive, Ref, watch } from "vue"
import { AciveClassSymbol, ChangeActiveSymbol, InitSymbol, IsActiveSymbol, ItemClassSymbol, ModelValueSymbol, Option, UnactiveSymbol } from "./constants"
import { defineHooks } from "@/components/hooks/define"

export const listProps = {
  modelValue: {
    type: valuePropType,
    default: () => undefined
  },
  activeClass: {
    type: classPropType,
    default: () => "active"
  },
  itemClass: {
    type: classPropType,
    default: () => ""
  },
  unactiveClass: {
    type: classPropType,
    default: () => ""
  },

  /**
   *  多选模式
   */
  multiple: {
    type: Boolean,
    default: () => false
  },

  /**
   *  是否可以反选
   *  在multiple模式下默认为true
   */
  deselect: {
    type: [Boolean] as PropType<boolean | undefined>,
    default: () => undefined
  },
  /**
   *  默认选择第一个
   *  在multiple模式下默认为false
   */
  defaultFirst: {
    type: Boolean as PropType<boolean | undefined>,
    default: () => undefined
  }
}

export const useSelectionList = defineHooks(listProps, (props, context) => {
  const options = reactive<Ref<Option>[]>([])

  function toArray(value: BaseType | BaseType[]) {
    return props.multiple && Array.isArray(value) ? [...value] : [value]
  }

  const actives = reactive<BaseType[]>(props.modelValue != undefined ? toArray(props.modelValue) : [])

  const deselect = computed(() => props.deselect ?? props.multiple)

  const defaultFirst = computed(() => props.defaultFirst ?? !props.multiple)

  watch(actives, val => {
    let value: BaseType | BaseType[] | undefined = undefined
    if (props.multiple) {
      value = options.filter(e => val.includes(e.value.value)).map(e => e.value.value)
    } else {
      value = options.find(e => val.includes(e.value.value))?.value.value
    }
    context.emit("change", value)
    context.emit("update:modelValue", value)
  })

  watch(
    () => props.modelValue,
    val => {
      actives.splice(0, actives.length, ...toArray(val))
    }
  )

  provide(
    AciveClassSymbol,
    computed(() => props.activeClass)
  )

  provide(
    UnactiveSymbol,
    computed(() => props.unactiveClass)
  )

  provide(
    ItemClassSymbol,
    computed(() => props.itemClass)
  )

  function isActive(value: BaseType) {
    return actives.includes(value)
  }

  function changeActive(option: BaseType) {
    if (isActive(option) && deselect.value) {
      actives.splice(actives.indexOf(option), 1)
    } else {
      if (!props.multiple) {
        actives.splice(0, actives.length, option)
      } else {
        actives.push(option)
      }
    }
  }

  provide(IsActiveSymbol, isActive)

  provide(ChangeActiveSymbol, changeActive)

  provide(InitSymbol, (option: Ref<Option>) => {
    options.push(option)

    if (option.value.value == props.modelValue || (actives.length == 0 && defaultFirst.value)) {
      actives.push(option.value.value)
    }

    return () => {
      const index = options.findIndex(e => e.value.value == option.value.value)
      if (index > -1) {
        options.splice(index, 1)
      }
    }
  })

  function render() {
    const children = options.filter(e => isActive(e.value.value)).map(e => e.value.render())
    return props.multiple ? children : children[0]
  }

  return {
    isActive,
    changeActive,
    render
  }
})
