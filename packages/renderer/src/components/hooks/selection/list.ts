import { classPropType, valuePropType } from "../types"
import { computed, provide, reactive, ref, Ref, watch } from "vue"
import { AciveClassSymbol, AciveSymbol, InitSymbol, ItemClassSymbol, ModelValueSymbol, Option, UnactiveSymbol } from "./constants"
import { defineHooks } from "@/components/hooks/define"

export const listProps = {
  value: {
    type: valuePropType,
    default: () => null
  },
  modelValue: {
    type: valuePropType,
    default: () => null
  },
  defaultValue: {
    type: valuePropType,
    default: () => null
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
  }
}

export const useSelectionList = defineHooks(listProps, (props, context) => {
  const current = ref<Option>()

  const modelValue = computed(() => props.modelValue)

  const options = reactive<Ref<Option>[]>([])

  const active = computed<Option | undefined>({
    set(val: Option | undefined) {
      current.value = val
      context.emit("update:modelValue", val?.value)
      context.emit("change", val?.value)
    },
    get() {
      return options.find(e => e.value.value == modelValue.value)?.value ?? current.value
    }
  })

  watch(active, val => {
    // console.log(val)
  })

  provide(ModelValueSymbol, modelValue)

  provide(AciveSymbol, active)

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

  provide(InitSymbol, (option: Ref<Option>) => {
    options.push(option)

    if (option.value.value == modelValue.value || active.value == undefined) {
      current.value = option.value
    }

    return () => {
      const index = options.findIndex(e => e.value.value == option.value.value)
      if (index > -1) {
        options.splice(index, 1)
      }
    }
  })

  function render() {
    return active.value?.render()
  }

  return {
    active,
    modelValue,
    render
  }
})
