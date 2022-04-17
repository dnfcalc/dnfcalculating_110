import { computed, ComputedRef, inject, onDeactivated, PropType, Ref, render, renderSlot, watch } from "vue"
import { defineHooks } from "../define"
import { AciveClassSymbol, AciveSymbol, InitSymbol, ItemClassSymbol, ModelValueSymbol, Option, UnactiveSymbol } from "./constants"
import { BaseType, ClassType, valuePropType } from "../types"

export const itemProps = {
    value: {
        type: valuePropType,
        required: true
    },
    label: {
        type: [Function, String] as PropType<string | ((val: BaseType) => string) | null>,
        default() {
            return null
        }
    }
}

export const useSelectionItem = defineHooks(itemProps, (props, { slots }) => {
    const active = inject(AciveSymbol) as Ref<Option>
    const init = inject<(obj: any) => () => void>(InitSymbol)
    const modelValue = inject(ModelValueSymbol) as Ref

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

    const current = computed(() => {
        return {
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

    watch(current, (newVal, oldVal) => {
        if (active && oldVal.value == modelValue.value) {
            active.value = newVal
        }
    })

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
