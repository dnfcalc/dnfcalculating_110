import { defineHooks } from "@/components/hooks/define"
import { syncRef } from "@vueuse/core"
import { computed, PropType, provide, reactive } from "vue"
import { BaseType, classPropType, labelPropType } from "../types"
import { AciveClassSymbol, ChangeActiveSymbol, InitSymbol, IsActiveSymbol, ItemClassSymbol, ItemLabelSymbol, Option, UnactiveSymbol } from "./constants"

export const listProps = {
  modelValue: {
    type: [String, Number, Array] as PropType<BaseType | BaseType[]>,
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
  label: {
    type: labelPropType,
    default: () => null
  },

  /**
   *  多选模式
   */
  multiple: {
    type: Boolean,
    default: () => false
  },

  multipleLimit: {
    type: Number,
    default: 0
  },

  defaultValue: {
    type: [String, Number, Array] as PropType<BaseType | BaseType[]>
  }
}

export const useSelectionList = defineHooks(listProps, (props, context) => {
  const options = reactive<Option[]>([])

  function toArray(value?: BaseType | BaseType[]): BaseType[] {
    if (value == undefined) {
      return []
    }
    if (props.multiple && Array.isArray(value)) {
      return value.filter(v => v != null || v != undefined)
    }
    return [value]
  }

  const actives: BaseType[] = reactive<BaseType[]>([...toArray(props.modelValue ?? props.defaultValue)])

  syncRef(
    computed({
      get() {
        return props.multiple ? actives : actives[0]
      },
      set(val) {
        if (props.multiple) {
          actives.splice(0, actives.length, ...toArray(val))
        } else {
          actives.splice(0, actives.length, val)
        }
      }
    }),
    computed({
      get() {
        return props.modelValue ?? props.defaultValue
      },
      set(val) {
        context.emit("update:modelValue", val)
        context.emit("change", val)
      }
    }),
    { immediate: true, deep: true }
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

  provide(ItemLabelSymbol, props.label)

  function isActive(value: BaseType) {
    return actives.includes(value)
  }

  function changeActive(option: BaseType) {
    if (isActive(option)) {
      if (props.multiple) {
        actives.splice(actives.indexOf(option), 1)
      }
    } else {
      if (props.multiple) {
        if (props.multipleLimit == 0 || props.multipleLimit > actives.length) {
          actives.push(option)
        }
      } else {
        actives.splice(0, actives.length, option)
      }
    }
  }

  provide(IsActiveSymbol, isActive)

  provide(ChangeActiveSymbol, changeActive)

  provide(InitSymbol, (option: Option) => {
    function remove() {
      const index = options.findIndex(e => e.id == option.id)
      if (index > -1) {
        options.splice(index, 1)
      }
    }
    for (let i = 0; i < options.length; i++) {
      if (options[i].value == option.value) {
        options.splice(i, 1)
        i--
      }
    }
    options.push(option)
    context.emit("load", option)
    return remove
  })

  function render() {
    const children = options.filter(e => actives.includes(e.value)).map(e => e.render())
    return props.multiple ? children : children[0]
  }

  return {
    options,
    actives,
    isActive,
    changeActive,
    render
  }
})
