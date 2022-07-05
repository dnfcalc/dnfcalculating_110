<script lang="tsx">
  import { useToggle, useVModel } from "@vueuse/core"
  import { defineComponent } from "vue"

  interface EqIconType {
    rarityClass?: string
    active?: boolean
    icon?: string
    id?: number
  }

  export default defineComponent({
    name: "eq-icon",
    props: {
      eq: {
        type: Object,
        default: () => {}
      },
      showTips: {
        type: Boolean,
        default: false
      },
      active: {
        type: Boolean,
        default: true
      },
      hightlight: {
        type: Boolean,
        default: false
      },
      badges: {
        type: Object,
        default: () => {
          return null
        }
      },
      hightlightClass: {
        type: String,
        default: "hightLight"
      }
    },
    setup(props, { emit }) {
      const active = useVModel(props, "active")
      const badgeClass = ["white", "red", "green", "blue", "yellow"]
      const toggle = useToggle(active)

      return () => {
        return (
          <div onClick={() => toggle()}>
            <div class={props.hightlight ? props.hightlightClass : ""}></div>
            <div class={active.value ? "" : "floatLayer"}></div>
            <div class="eq-item-box">
              {props.eq && props.eq.icon ? (
                <div
                  class={["eq-icon"].concat([
                    props.eq.rarityClass ?? "epic"
                    // eq.value.active ? '' : 'gray'
                  ])}
                >
                  <img src={"/images/equipment/" + props.eq.icon} />
                  {true || props.badges == null ? (
                    <div></div>
                  ) : props.badges.color[0] == 0 ? (
                    props.badges.num == 0 ? (
                      <div class="left kong-box">
                        <div class="kong-item"></div>
                      </div>
                    ) : (
                      <div class="left kong-box">
                        <div class={["kong-item"].concat([badgeClass[props.badges.color[0]]])}></div>
                      </div>
                    )
                  ) : props.badges.num == 0 ? (
                    <div class="kong-box">
                      <div class="kong-item"></div>
                      <div class="kong-item"></div>
                    </div>
                  ) : props.badges.num == 1 ? (
                    <div class="kong-box">
                      <div class={["kong-item"].concat([badgeClass[props.badges.color[0]]])}></div>
                      <div class="kong-item"></div>
                    </div>
                  ) : (
                    <div class="kong-box">
                      <div class={["kong-item"].concat([badgeClass[props.badges.color[0]]])}></div>
                      <div class={["kong-item"].concat([badgeClass[props.badges.color[1]]])}></div>
                    </div>
                  )}
                </div>
              ) : (
                <span class="icon"></span>
              )}
            </div>
          </div>
        )
      }
    }
  })
</script>
<style scoped lang="scss">
  .eq-item-box {
    width: 30px;
    height: 30px;
    display: inline-block;
  }

  .floatLayer {
    position: absolute;
    width: 30px;
    height: 30px;
    z-index: 2;
    background-color: #00000080;
  }

  .hightLight {
    position: absolute;
    width: 30px;
    height: 30px;
    z-index: 3;
    background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDcuMS1jMDAwIDc5LmRhYmFjYmIsIDIwMjEvMDQvMTQtMDA6Mzk6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMy4wIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpGMjlBNkIyMUE0NTgxMUVDOTMwM0UwOTYyOTA5Q0M2RCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpGMjlBNkIyMkE0NTgxMUVDOTMwM0UwOTYyOTA5Q0M2RCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkYyOUE2QjFGQTQ1ODExRUM5MzAzRTA5NjI5MDlDQzZEIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkYyOUE2QjIwQTQ1ODExRUM5MzAzRTA5NjI5MDlDQzZEIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+7pxKFgAABXFJREFUeNrEV0uS40QQzdTf3e6mpyfgCLBmzXU4FZdiSXCBIWCAjplu27KkquTlq5JcNrMfK0rfrHz5z7SamXyNX+Mn/eVtkO+rgywSZbIgo+RlUU64niHdWUwmrBn3AZtWeWtfqtKJSu8L93e4DlrJgK++etx3uDZSyW/xW/t5/y+BCRp4zIA+Y9sEsnUFkC+4Rlyx1MTNZBm6AnWNVeWj5lPDO5UWFB0oe+zswKmRH6qPLmoCnvA6OqiNeHrFpjdsw9JRWjtL0FmCLdgWxPVVvQDXhKgAUUurWKDqANTi3Li+ugfVPXbtgTG4gTdTw5SLn7E+g8VfePs3ri+4fgazozQAbwA+QrgJtIGCGljoBtqrw7QwcS873PUweKMPoHgHvu8psu8w0G/A7k8FcAVtO/kIsA/48ie+fAKLV6wRX2c5QYBJF1jIoYUsHNh122kLQOgK4MFBoaHJEyhP4mrNNmBPMvkFGAFV6QR5D3jzQtBB/gCTf2j6CZvP4qABGs+4C9S4ojc1A3fYD3Dd+RnfHyDqEcK6K3cAf4fnR0bSBnwCWW2uB8yqn8DyhaAP0L7Xg5ieADhy0+T+pr4psJQh1KQDWru+ERpPsM4bed/JYk+w2RFaT8ycK+BG3HcTrkfIBzD4t9NXyHiANZxiYQBajn/mYT5SeCGS1ZMKYiEOXhGAYj12vAL0AKtO4rBLqfHZIl949HognV06kBui2kF32CL4JtzkK95kcizeRRmZcjV4HsH7SEeN4OEuCqlirelkzNMIX3v0nkh0hokmappAlwxqGWT9rYCWU8Xo/QDPny0BnszXwioR5ApYCOwmbEAwAmQE2EzTLoVGq8ay5mN+X+X7mcDRfUnTuu0QlJ6GuTxdAS9rJVL3YqAvPF+jeuzGrG1p3lVrLTS3zC+S/URNkQFYo82Zr1u1AI55ozJJEvOFYZSYXJtXi/u4mTf9Ap+NRTYpMNOOlrS1lftmokuESvbS9c9u7rWwgP7PEpaPhfayXOfSEUvgKm+vmBpJgCaXQ+XX6sasazRXxbMW6/qnxVEVbTGVPtUN2Gtvh9pb5xaQQL6k/artKkC1wfjuNme4Zr6OEa0AblXXEoAi74XeC36qRkqacANaplCpdareSpG9cYCXNcgQlCdLAgQtulOXzUpC7zAofGxtKPhewxPAnJkvNwF2a+aG/aqVxMt5dgCfcteuy7bY0wwA9okBZc+BBx0A3oF0V5jUbqI5btGR3NEkYG05b7Tm4B27VoDWk/koUQDvNE0OPfsKmpruSF5j6VU51Kz5cqNltYEKPduzWbjwVALcZnOBKjbgC3D2Sg9tdwS9w/Y7fvGSec6aubRGqatLYmzx6owbTl7RenaorAbPM6eu+ksau1d6gvrkIGiKXurQKXIldz+1kBw1HNeFWq+JlXY3dE4L2nuY9QH7HvHlHhlyR3M3/FZMIMO6lU3cQZ/YnY4APToY+9PIou/Hic0jVTZmg9ZMnx009QmkobV8EHgmrxr3yXUtd1yAtcqTkw+mTzAVmKv36QFl7oFNfMRxYrcBNLrYkls6vQv/9VrTXg4+QIEG2gpHn+/Is9V70N0A93zwpHJJnxk+7qdFvoGmBwCOBDxR44XD4ZL7jBZzF4NTE3gPE7f6iC/PHPbc5OLpWZq6ZbD4/Ltn1AUGwxP8dMqAPnXN7KmX9hYLH1egVbz3OabBNU2bg7ln93DFHjS+UoBtwDWBm22gCQz/ewaXa+eTw5mAgR267DQuf9SUUlUx1lcwf60tbZEqRC8pEgqNf6xr+TUEpoTx/0JLrdOUlaatwL8uaXlPjUUjdAm8FNJa0HzhffoPEnOtV2bGLL/H9/ITtPtaf9r+E2AA4bfLT+prOiQAAAAASUVORK5CYII=);
    background-size: 100% 100%;
  }

  .hightLight2 {
    position: absolute;
    width: 30px;
    height: 30px;
    z-index: 3;
    background-image: url("@/assets/img/item_checked.png");
    background-size: 100% 100%;
  }
  .eq-icon {
    width: 30px;
    height: 30px;
    position: relative;
    display: inline-block;
    border-radius: 3px;

    &.gray {
      -webkit-filter: grayscale(100%);
      -moz-filter: grayscale(100%);
      -ms-filter: grayscale(100%);
      -o-filter: grayscale(100%);
      filter: grayscale(100%);
      filter: gray;
    }

    &::before {
      content: "";
      width: 28px;
      height: 28px;
      display: inline-block;
      position: absolute;
      background-color: rgba($color: #000000, $alpha: 1);
      top: 1px;
      left: 1px;
    }

    &::after {
      content: "";
      width: 27px;
      height: 27px;
      position: absolute;
      top: 0;
      left: 0;
      border: 1.5px solid;
      border-image: linear-gradient(red, #000) 1;
      clip-path: inset(0 round 2px);
    }

    &.normal {
      &::after {
        border-image: linear-gradient(#e7a300, #000) 1;
      }
    }
    &.advanced {
      &::after {
        border-image: linear-gradient(#61c8de, #000) 1;
      }
    }
    &.rare {
      &::after {
        border-image: linear-gradient(#a060e4, #000) 1;
      }
    }
    &.artifact {
      &::after {
        border-image: linear-gradient(#ef00ef, #000) 1;
      }
    }
    &.legend {
      &::after {
        border-image: linear-gradient(#e96e00, #000) 1;
      }
    }
    &.epic {
      &::after {
        border-image: linear-gradient(#e7a300, #000) 1;
      }
    }
    &.myth {
      &::after {
        border-image: linear-gradient(#f8c63d, #cc66e7) 1;
      }
    }
    // &.can-click:hover {
    //   cursor: pointer;
    //   background-image: linear-gradient(#3ae7fa, #3ae7fa);
    // }

    > img {
      position: relative;
      top: 0;
      left: 0;
      width: 30px;
      height: 30px;
      border-radius: 2px;
    }

    .kong-box {
      width: 14px;
      height: 7px;
      position: absolute;
      bottom: 1px;
      right: -1px;
      display: flex;

      &.left {
        right: auto;
        left: 0;
        width: 7px;
      }

      .kong-item {
        width: 7px;
        position: relative;
        border: 1px solid #637b39;
        background-color: #522910;
        &::after {
          content: "";
          display: block;
          height: 3px;
          border: 1px solid rgba(#000, 0.5);
        }

        &:last-child {
          right: 1px;
        }

        &.red {
          background: linear-gradient(to left top, #ff108c, #ff73c6, #ad0852, #ff108c, #ffffff, #ffffff);
        }
        &.blue {
          background: linear-gradient(to left top, #10ceff, #73e7ff, #086bad, #10ceff, #ffffff, #ffffff);
        }
        &.green {
          background: linear-gradient(to left top, #b5ff10, #efff73, #63ad08, #b5ff10, #ffffff, #ffffff);
        }
        &.yellow {
          background: linear-gradient(to left top, #ffbd10, #ffd673, #ad6308, #ffbd10, #ffffff, #ffffff);
        }
        &.white {
          border: 1px solid #ffde5a;
          background: linear-gradient(to left top, #efffff, #ceffff, #4a7bde, #efffff, #efffff, #ffffff);
        }
      }
    }
  }
</style>
