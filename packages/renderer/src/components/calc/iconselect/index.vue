<script lang="tsx">
  /**
   * @Author: Kritsu
   * @Date:   2021/11/09 15:31:30
   * @Last Modified by:   Kritsu
   * @Last Modified time: 2021/11/17 18:49:23
   */
  import {
    defineComponent,
    ref,
    computed,
    watch,
    Teleport,
    onDeactivated,
    renderSlot,
    CSSProperties,
    Transition
  } from "vue"
  import {
    listProps,
    useSelectionList
  } from "@/components/hooks/selection/list"

  import NSelection from "@/components/base/selection"
  import { onClickOutside } from "@vueuse/core"

  export default defineComponent({
    name: "i-iconselect",
    props: {
      ...listProps,
      disabled: {
        type: Boolean,
        default: false
      },
      width: {
        type: Number,
        default: 120
      },
      emptyLabel: {
        type: String
      }
    },
    components: {
      NSelection
    },
    setup(props, context) {
      const { active } = useSelectionList(
        { ...props, itemClass: "i-select-dropdown-item" },
        context
      )
      console.log({ ...props })

      const isOpen = ref(false)
      const triggerRef = ref<HTMLElement>()

      watch(isOpen, onResize)

      function collapse() {
        isOpen.value = !isOpen.value && !isDisabled.value
      }

      // 下拉框位置
      const dropdownPosition = ref({ x: 0, y: 0, w: 0 })
      // 下拉框位置
      const dropdownStyle = computed<CSSProperties>(() => {
        return {
          left: `${dropdownPosition.value.x}px`,
          top: `${dropdownPosition.value.y}px`,
          width: `${dropdownPosition.value.w}px`
        }
      })

      function onResize() {
        if (!!triggerRef.value) {
          const { width, height, left, top } =
            triggerRef.value.getBoundingClientRect()
          dropdownPosition.value = {
            w: width,
            x: left,
            y: top + height + 2
          }
        }
      }

      const isDisabled = computed(() => !!props.disabled)

      onClickOutside(triggerRef, () => (isOpen.value = false))

      window.addEventListener("resize", onResize)
      window.addEventListener("scroll", onResize)

      onDeactivated(() => {
        window.removeEventListener("resize", onResize)
        window.removeEventListener("scroll", onResize)
      })

      const { slots } = context
      console.log(active.value?.render())
      console.log(active.value)
      console.log(active.value?.render() ?? props.emptyLabel)

      return () => {
        return (
          <div class="i-icon-select" onClick={collapse}>
            <div
              class={{
                "i-select-trigger": true,
                disabled: props.disabled
              }}
              ref={triggerRef}
            >
              <span class="i-select-label">
                {active.value?.render() ?? props.emptyLabel}
              </span>
            </div>
            <Teleport to="body">
              <Transition name="dropdown" mode="out-in">
                <div
                  class="i-icon-select-dropdown"
                  style={dropdownStyle.value}
                  v-show={isOpen.value}
                >
                  {renderSlot(slots, "default")}
                </div>
              </Transition>
            </Teleport>
          </div>
        )
      }
    }
  })
</script>
<style lang="scss">
  /**
  * @Author: Kritsu
  * @Date:   2021/11/09 15:43:10
  * @Last Modified by:   Kritsu
  * @Last Modified time: 2021/11/17 18:03:08
  */
  $text-color: #e9c556;
  .i-icon-select {
    width: 28px;
    min-width: 28px;
    user-select: none;
    outline: none;
    height: 28px;
    line-height: 100%;
    font-size: 12px;
    color: $text-color;
    background-color: rgba(0, 0, 0, 1);
    border: 1px solid #5b472a;
    border-radius: 2px;
    padding: 0;
    margin: 0;
    display: block;

    .i-select-trigger {
      padding: 0;
      display: flex;
      height: 100%;
      opacity: 0.8;

      justify-content: center;
      align-items: center;

      &.disabled {
        color: gray;
      }
    }

    .i-select-trigger:hover {
      opacity: 1;
    }
  }

  .i-icon-select-dropdown {
    position: fixed;
    overflow-y: auto;
    background: black;
    font-size: 12px;
    z-index: 888;
    min-height: 28px;

    $hoverColor: #002947;
    $activeColor: lighten($hoverColor, 5%);
    color: $text-color;

    .i-select-dropdown-item {
      font-size: 12px;
      height: 28px;
      line-height: 28px;
      margin: 0;
      border: none;
      outline: none;
      appearance: none;
      display: block;
      overflow: hidden;

      &.active {
        background-color: $activeColor;
      }

      &:hover:not(.active) {
        font-size: 12px;
        background-color: $hoverColor;
      }
    }
  }

  .dropdown-active {
    animation: dropdown-enter 0.2s ease-in;
  }

  .dropdown-active {
    animation: dropdown-leave 0.2s ease-in;
  }

  .dropdown-enter-active {
    animation: dropdown-enter 0.2s ease-in;
  }

  .dropdown-leave-active {
    animation: dropdown-leave 0.2s ease-in;
  }

  .dropdown-enter-active {
    animation: dropdown-enter 0.2s ease-in;
  }

  .dropdown-leave-active {
    animation: dropdown-leave 0.2s ease-in;
  }
</style>
