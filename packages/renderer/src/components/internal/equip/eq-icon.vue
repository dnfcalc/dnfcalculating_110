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
      hightlightclass: {
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
            <div class={props.hightlight ? props.hightlightclass : ""}></div>
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
                      <div class="kong-box left">
                        <div class="kong-item"></div>
                      </div>
                    ) : (
                      <div class="kong-box left">
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
    background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAdCAYAAAC5UQwxAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAFyGlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNi4wLWMwMDIgNzkuMTY0NDYwLCAyMDIwLzA1LzEyLTE2OjA0OjE3ICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgMjEuMiAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDIyLTA0LTE1VDIzOjA2OjU0KzA4OjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDIyLTA0LTE1VDIzOjA2OjU0KzA4OjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMi0wNC0xNVQyMzowNjo1NCswODowMCIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpjYjU5MTMxNy02Yjc0LTc4NGQtYjQ1Ni1hMzc3Y2RkMGFkMTYiIHhtcE1NOkRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDozNzdkZjI5NS05NDkzLTRlNDUtYjk4NC01NTVhNTFjMjQzNzciIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDoyMGQ3NTgyMy03NGY3LWVhNGQtOWNjMy0yODE1NTZjNjFmYjgiIGRjOmZvcm1hdD0iaW1hZ2UvcG5nIiBwaG90b3Nob3A6Q29sb3JNb2RlPSIzIj4gPHhtcE1NOkhpc3Rvcnk+IDxyZGY6U2VxPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0iY3JlYXRlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDoyMGQ3NTgyMy03NGY3LWVhNGQtOWNjMy0yODE1NTZjNjFmYjgiIHN0RXZ0OndoZW49IjIwMjItMDQtMTVUMjM6MDY6NTQrMDg6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCAyMS4yIChXaW5kb3dzKSIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6Y2I1OTEzMTctNmI3NC03ODRkLWI0NTYtYTM3N2NkZDBhZDE2IiBzdEV2dDp3aGVuPSIyMDIyLTA0LTE1VDIzOjA2OjU0KzA4OjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgMjEuMiAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+O3vJjQAAAhJJREFUSIntlr9rE2EYxz9PmsilnjXFq0ZzgagRTrjhFU4NclM3F5duTm5FEFxEcFAQioggDgp1cNA/wMnRXSgKIg4ZREG0dFFwMb02lsehl7epuSbVxg7aB77D+z4P7+d9frzHiaqynZbbVtoOcAfYz0RkWkS+isjsicOFo9ahqkMXcAXQbo25uXFVHT4QuAaozlatUuiUqg63pCJyA7ilD6qwAqyAXPwEsLyrkH8BQ+yhiMwAN/VeFdpAG+TSKswYc2Zpub0ADKekwG1A9U7VitUyLsVxHK2L3QoojhsC3AVUZ6pWKSyJoijqudyvG4cO5I8Bz4H3wLPSaG4sGxYJcB9Qve5bdWBxHJ/MrEb3wnPYDySsH+lmHHn7uuOimiPAQ0D1qm+Vxi96npcJ6wECEaB62bdKD/lgyvkJVaURuCPAow3iFssl91TffncvTOAUgAVAddq3Sg+bj0PnOPBkA3/LhMHpQX2XNDNr48Vi5VuSvAQO6gV/bewffwb4AeQz9lsmqE++br6bG/h+sm7RCNwy8BFQPV+xyloD300YNjY72T0ZdmyiWPS+JMkccESnKj1+eToP0AqDYPJtszk4s34Z2p6GZi/QBFTPVaw6mYXB4J4NfIc95TVmD/AGUD27BguC+m/DNv2lqZWcUeBVB1ar1fuO/paBqorv5gXYHYbhyJ/C+g7N37J/55/m/wX+BAPinG1rXvIhAAAAAElFTkSuQmCC);
    background-size: 100% 100%;
  }
  .eq-icon {
    width: 30px;
    height: 30px;
    background-image: linear-gradient(#e66465, #000);
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

    &.normal {
      background-image: linear-gradient(#ffffff, #000);
    }
    &.advanced {
      background-image: linear-gradient(#61c8de, #000);
    }
    &.rare {
      background-image: linear-gradient(#a060e4, #000);
    }
    &.artifact {
      background-image: linear-gradient(#ef00ef, #000);
    }
    &.legend {
      background-image: linear-gradient(#e96e00, #000);
    }
    &.epic {
      background-image: linear-gradient(#e7a300, #000);
    }
    &.myth {
      background-image: linear-gradient(#e7a300, #000);
    }

    // &.can-click:hover {
    //   cursor: pointer;
    //   background-image: linear-gradient(#3ae7fa, #3ae7fa);
    // }

    > img {
      position: relative;
      top: 1px;
      left: 1px;
      width: 28px;
      height: 28px;
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
