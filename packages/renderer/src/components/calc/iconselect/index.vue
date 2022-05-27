<script lang="tsx">
  /**
   * @Author: Kritsu
   * @Date:   2021/11/09 15:31:30
   * @Last Modified by:   Kritsu
   * @Last Modified time: 2021/11/17 18:49:23
   */
  import { defineComponent, ref, computed, watch, Teleport, onDeactivated, renderSlot, CSSProperties, Transition, render, Fragment, reactive } from "vue"
  import { listProps, useSelectionList } from "@/components/hooks/selection/list"

  import { onClickOutside, reactifyObject } from "@vueuse/core"

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
    font-size: 12px;
    z-index: 888;
    min-height: 28px;

    $hoverColor: #002947;
    $activeColor: lighten($hoverColor, 5%);
    color: $text-color;

    .i-option {
      font-size: 12px;
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
        background-image: url("./img/active.png");
        background-size: 100% 100%;
        z-index: 3;
      }

      &:hover:not(.active) ::before {
        content: "";
        width: 28px;
        height: 28px;
        position: absolute;
        background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDcuMS1jMDAwIDc5LmRhYmFjYmIsIDIwMjEvMDQvMTQtMDA6Mzk6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMy4wIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpGMjlBNkIyMUE0NTgxMUVDOTMwM0UwOTYyOTA5Q0M2RCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpGMjlBNkIyMkE0NTgxMUVDOTMwM0UwOTYyOTA5Q0M2RCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkYyOUE2QjFGQTQ1ODExRUM5MzAzRTA5NjI5MDlDQzZEIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkYyOUE2QjIwQTQ1ODExRUM5MzAzRTA5NjI5MDlDQzZEIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+7pxKFgAABXFJREFUeNrEV0uS40QQzdTf3e6mpyfgCLBmzXU4FZdiSXCBIWCAjplu27KkquTlq5JcNrMfK0rfrHz5z7SamXyNX+Mn/eVtkO+rgywSZbIgo+RlUU64niHdWUwmrBn3AZtWeWtfqtKJSu8L93e4DlrJgK++etx3uDZSyW/xW/t5/y+BCRp4zIA+Y9sEsnUFkC+4Rlyx1MTNZBm6AnWNVeWj5lPDO5UWFB0oe+zswKmRH6qPLmoCnvA6OqiNeHrFpjdsw9JRWjtL0FmCLdgWxPVVvQDXhKgAUUurWKDqANTi3Li+ugfVPXbtgTG4gTdTw5SLn7E+g8VfePs3ri+4fgazozQAbwA+QrgJtIGCGljoBtqrw7QwcS873PUweKMPoHgHvu8psu8w0G/A7k8FcAVtO/kIsA/48ie+fAKLV6wRX2c5QYBJF1jIoYUsHNh122kLQOgK4MFBoaHJEyhP4mrNNmBPMvkFGAFV6QR5D3jzQtBB/gCTf2j6CZvP4qABGs+4C9S4ojc1A3fYD3Dd+RnfHyDqEcK6K3cAf4fnR0bSBnwCWW2uB8yqn8DyhaAP0L7Xg5ieADhy0+T+pr4psJQh1KQDWru+ERpPsM4bed/JYk+w2RFaT8ycK+BG3HcTrkfIBzD4t9NXyHiANZxiYQBajn/mYT5SeCGS1ZMKYiEOXhGAYj12vAL0AKtO4rBLqfHZIl949HognV06kBui2kF32CL4JtzkK95kcizeRRmZcjV4HsH7SEeN4OEuCqlirelkzNMIX3v0nkh0hokmappAlwxqGWT9rYCWU8Xo/QDPny0BnszXwioR5ApYCOwmbEAwAmQE2EzTLoVGq8ay5mN+X+X7mcDRfUnTuu0QlJ6GuTxdAS9rJVL3YqAvPF+jeuzGrG1p3lVrLTS3zC+S/URNkQFYo82Zr1u1AI55ozJJEvOFYZSYXJtXi/u4mTf9Ap+NRTYpMNOOlrS1lftmokuESvbS9c9u7rWwgP7PEpaPhfayXOfSEUvgKm+vmBpJgCaXQ+XX6sasazRXxbMW6/qnxVEVbTGVPtUN2Gtvh9pb5xaQQL6k/artKkC1wfjuNme4Zr6OEa0AblXXEoAi74XeC36qRkqacANaplCpdareSpG9cYCXNcgQlCdLAgQtulOXzUpC7zAofGxtKPhewxPAnJkvNwF2a+aG/aqVxMt5dgCfcteuy7bY0wwA9okBZc+BBx0A3oF0V5jUbqI5btGR3NEkYG05b7Tm4B27VoDWk/koUQDvNE0OPfsKmpruSF5j6VU51Kz5cqNltYEKPduzWbjwVALcZnOBKjbgC3D2Sg9tdwS9w/Y7fvGSec6aubRGqatLYmzx6owbTl7RenaorAbPM6eu+ksau1d6gvrkIGiKXurQKXIldz+1kBw1HNeFWq+JlXY3dE4L2nuY9QH7HvHlHhlyR3M3/FZMIMO6lU3cQZ/YnY4APToY+9PIou/Hic0jVTZmg9ZMnx009QmkobV8EHgmrxr3yXUtd1yAtcqTkw+mTzAVmKv36QFl7oFNfMRxYrcBNLrYkls6vQv/9VrTXg4+QIEG2gpHn+/Is9V70N0A93zwpHJJnxk+7qdFvoGmBwCOBDxR44XD4ZL7jBZzF4NTE3gPE7f6iC/PHPbc5OLpWZq6ZbD4/Ltn1AUGwxP8dMqAPnXN7KmX9hYLH1egVbz3OabBNU2bg7ln93DFHjS+UoBtwDWBm22gCQz/ewaXa+eTw5mAgR267DQuf9SUUlUx1lcwf60tbZEqRC8pEgqNf6xr+TUEpoTx/0JLrdOUlaatwL8uaXlPjUUjdAm8FNJa0HzhffoPEnOtV2bGLL/H9/ITtPtaf9r+E2AA4bfLT+prOiQAAAAASUVORK5CYII=);
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
