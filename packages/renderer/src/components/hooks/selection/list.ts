import { classPropType, valuePropType } from "./types"
import { computed, provide, ref, SetupContext, ComponentPropsOptions, Ref, watch } from "vue"
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

export const useSelectionList = defineHooks(listProps, (props, context, selectType = 0) => {
    const current = ref<Option>()

    const modelValue = computed(() => props.modelValue)

    const options: Ref<Option>[] = []

    const active = computed<Option | undefined>({
        set(val: Option | undefined) {
            context.emit("update:modelValue", val?.value)
            context.emit("change", val?.value)
            current.value = val
        },
        get() {
            return options.find(e => e.value.value == modelValue.value)?.value ?? current.value
        }
    })

    watch(active, val => {
        console.log(val)
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
        selectType == 0 ? ItemClassSymbol : "i-select-dropdown-item",
        computed(() => props.itemClass)
    )

    provide(InitSymbol, (option: Ref<Option>) => {
        options.push(option)
        // if (option.value.value == modelValue.value || active.value == undefined) {
        if (option.value.value == modelValue.value) {
            current.value = option.value
        }
        return () => {
            options.splice(options.indexOf(option), 1)
        }
    })

    function render() {
        const option = options.find(e => e.value.value == modelValue.value)
        console.log(option, options, modelValue.value, props.modelValue)
        if (option) {
            const tmp = option.value.render()
            return tmp
        }
    }

    return {
        active,
        modelValue,
        render
    }
})
