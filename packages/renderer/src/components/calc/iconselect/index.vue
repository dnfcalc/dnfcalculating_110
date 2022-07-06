<script lang="tsx">
  /**
   * @Author: Kritsu
   * @Date:   2021/11/09 15:31:30
   * @Last Modified by:   Kritsu
   * @Last Modified time: 2021/11/17 18:49:23
   */
  import { listProps, useSelectionList } from "@/components/hooks/selection/list"
  import { computed, CSSProperties, defineComponent, onDeactivated, ref, renderSlot, Teleport, Transition, watch } from "vue"

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
        default: 28
      },
      emptyLabel: {
        type: String
      },
      columnNum: {
        type: Number,
        default: 1
      }
    },
    setup(props, context) {
      // props.itemClass = "i-select-dropdown-item"
      // const { active } = useSelectionList({ ...props, itemClass: "i-select-dropdown-item" }, context)
      const { render } = useSelectionList(() => {
        return {
          ...props,
          itemClass: "i-option"
        }
      }, context)

      // const { active } = useSelectionList(props, context)
      const columnNum = computed(() => props.columnNum || 1)
      // console.log({ ...props })

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
          width: `${columnNum.value * 32}px`
        }
      })

      function onResize() {
        if (!!triggerRef.value) {
          const { width, height, left, top } = triggerRef.value.getBoundingClientRect()
          dropdownPosition.value = {
            w: width,
            x: left - 2,
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
      // console.log(active.value?.render())
      // console.log(active.value)
      // console.log(active.value?.render() ?? props.emptyLabel)

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
              <span class="i-select-label">{render() ?? props.emptyLabel}</span>
            </div>
            <Teleport to="body">
              <Transition name="dropdown" mode="out-in">
                <div class="i-icon-select-dropdown" style={dropdownStyle.value} v-show={isOpen.value}>
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
    // font-size: 12px;
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
      opacity: 1;

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
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    position: fixed;
    overflow-y: hidden;
    overflow-x: hidden;
    // background: rgba(255, 255, 255, 0.1);
    // font-size: 12px;
    z-index: 888;
    min-height: 28px;

    $hoverColor: #002947;
    $activeColor: lighten($hoverColor, 5%);
    color: $text-color;

    .i-option {
      // font-size: 12px;
      height: 28px;
      line-height: 28px;
      margin: 1px;
      border: none;
      outline: none;
      appearance: none;
      display: block;
      overflow: hidden;
      border: gray 1px solid;

      // &.active {
      //     background-color: $activeColor;
      // }

      &.active::before {
        content: "";
        width: 28px;
        height: 28px;
        position: absolute;
        background-image: url("/src/assets/img/item_checked.png");
        background-size: 80% 80%;
        background-repeat: no-repeat;
        background-position: center;
        z-index: 3;
      }

      &:hover:not(.active) ::before {
        content: "";
        width: 28px;
        height: 28px;
        position: absolute;
        background-image: url("@/assets/img/item_hover.png");
        background-size: 100% 100%;
        z-index: 3;
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
