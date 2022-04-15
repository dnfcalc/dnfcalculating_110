import type { ComponentPropsOptions, SetupContext } from "vue"

export function defineHooks<P extends object, R>(_: ComponentPropsOptions<P>, setup: (props: P, context: SetupContext) => R) {
    return (props: P | (() => P), context: SetupContext) => {
        let p = props instanceof Function ? props() : props
        return setup(p, context)
    }
}
