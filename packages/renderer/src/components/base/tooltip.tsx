/**
 * @Author: Kritsu
 * @Date:   2021/11/16 23:07:51
 * @Last Modified by:   Kritsu
 * @Last Modified time: 2021/11/17 18:49:42
 */
import { watch, defineComponent, renderSlot, Teleport, ref, computed, CSSProperties, Transition, PropType, reactive, nextTick } from "vue"

export const tooltipProps = {
  popClass: {
    type: String
  },
  position: {
    type: String as PropType<"bottom" | "top" | "left" | "right">,
    default: () => "bottom"
  },
  offset: {
    type: Number,
    default: () => 4
  },
  lazy: {
    type: Boolean,
    default: () => false
  }
}

export default defineComponent({
  name: "i-tooltip",
  emits: ["change"],
  props: tooltipProps,
  setup(props, { slots, emit }) {
    const isOpen = ref(false)
    let timer: NodeJS.Timeout

    const triggerRef = ref<HTMLElement>()
    const popupRef = ref<HTMLElement>()

    const dropdownPosition = reactive({ x: 0, y: 0 })

    const isShow = computed(() => isOpen.value && triggerRef.value && popupRef.value && dropdownPosition.x + dropdownPosition.y > 0)

    const dropdownStyle = computed<CSSProperties>(() => {
      return {
        left: `${dropdownPosition.x}px`,
        top: `${dropdownPosition.y}px`,
        visibility: isShow.value ? "visible" : "hidden"
      }
    })

    const mounted = ref(false)

    function onMouseover() {
      timer = setTimeout(
        function () {
          isOpen.value = true
        },
        props.lazy ? 800 : 100
      )
    }

    function onMouseout() {
      clearTimeout(timer)
      isOpen.value = false
    }

    function resize() {
      const trigger = triggerRef.value
      const popup = popupRef.value

      if (!!trigger && !!popup) {
        const { width, height, left, top } = trigger.getBoundingClientRect()

        const { clientWidth: pWidth, clientHeight: pHeight } = popup

        let x = 0
        let y = 0

        const offset = props.offset
        switch (props.position) {
          case "bottom":
            x = left + width / 2
            y = top + height + offset
            break
          case "top":
            x = left
            y = top - pHeight - offset
            break
          case "left":
            x = left - pWidth - offset
            y = top
            break
          case "right":
            x = left + width + offset
            y = top
            break
        }
        x = window.innerWidth - x > 500 ? x + 20 : x - 20 - 310
        y = window.innerHeight - y > popup.offsetHeight + 50 ? y : window.innerHeight - (popup.offsetHeight + 50)
        dropdownPosition.x = x
        dropdownPosition.y = y
      }
    }

    watch(isOpen, val => {
      if (val) {
        mounted.value = true
      }
      emit("change", val)
      nextTick(resize)
    })

    return () => {
      return (
        <div class="flex items-center" {...{ onMouseout, onMouseover }} ref={triggerRef}>
          {renderSlot(slots, "default")}
          <Teleport to="body">
            <Transition name="dropdown" mode="out-in">
              {mounted.value && (
                <div class={["i-popper z-999", props.popClass]} style={dropdownStyle.value} ref={popupRef}>
                  {renderSlot(slots, "popper")}
                </div>
              )}
            </Transition>
          </Teleport>
        </div>
      )
    }
  }
})
