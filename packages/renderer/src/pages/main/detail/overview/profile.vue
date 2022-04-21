<script lang="tsx">
  import { computed, Ref, defineComponent, inject, renderList, PropType } from "vue"
  import { useVModel } from "@vueuse/core"
  import { useCharacterStore, useDetailsStore } from "@/store"
  export default defineComponent({
    name: "profile",
    setup(props, { emit, slots }) {
      //面板显示的顺序

      const characterStore = useCharacterStore()

      const detailsStore = useDetailsStore()
      const display_parts = detailsStore.display_parts

      function partIconStyle(part: string) {
        let x = 10
        let y = 10
        let index = display_parts.findIndex(p => p == part)
        let active = index == display_parts.findIndex(p => p == detailsStore.part)

        if (index == 13) index -= 7
        else if (index >= 5 && index <= 12) {
          x += 189
          index -= 5
        }

        x += (index % 2) * 32
        y += Math.floor(index / 2) * 32

        let style = active
          ? {
              left: `${x}px`,
              top: `${y}px`,
              zIndex: 3,
              backgroundSize: "100% 100%",
              backgroundImage:
                "url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDcuMS1jMDAwIDc5LmRhYmFjYmIsIDIwMjEvMDQvMTQtMDA6Mzk6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMy4wIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpGMjlBNkIyMUE0NTgxMUVDOTMwM0UwOTYyOTA5Q0M2RCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpGMjlBNkIyMkE0NTgxMUVDOTMwM0UwOTYyOTA5Q0M2RCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkYyOUE2QjFGQTQ1ODExRUM5MzAzRTA5NjI5MDlDQzZEIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkYyOUE2QjIwQTQ1ODExRUM5MzAzRTA5NjI5MDlDQzZEIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+7pxKFgAABXFJREFUeNrEV0uS40QQzdTf3e6mpyfgCLBmzXU4FZdiSXCBIWCAjplu27KkquTlq5JcNrMfK0rfrHz5z7SamXyNX+Mn/eVtkO+rgywSZbIgo+RlUU64niHdWUwmrBn3AZtWeWtfqtKJSu8L93e4DlrJgK++etx3uDZSyW/xW/t5/y+BCRp4zIA+Y9sEsnUFkC+4Rlyx1MTNZBm6AnWNVeWj5lPDO5UWFB0oe+zswKmRH6qPLmoCnvA6OqiNeHrFpjdsw9JRWjtL0FmCLdgWxPVVvQDXhKgAUUurWKDqANTi3Li+ugfVPXbtgTG4gTdTw5SLn7E+g8VfePs3ri+4fgazozQAbwA+QrgJtIGCGljoBtqrw7QwcS873PUweKMPoHgHvu8psu8w0G/A7k8FcAVtO/kIsA/48ie+fAKLV6wRX2c5QYBJF1jIoYUsHNh122kLQOgK4MFBoaHJEyhP4mrNNmBPMvkFGAFV6QR5D3jzQtBB/gCTf2j6CZvP4qABGs+4C9S4ojc1A3fYD3Dd+RnfHyDqEcK6K3cAf4fnR0bSBnwCWW2uB8yqn8DyhaAP0L7Xg5ieADhy0+T+pr4psJQh1KQDWru+ERpPsM4bed/JYk+w2RFaT8ycK+BG3HcTrkfIBzD4t9NXyHiANZxiYQBajn/mYT5SeCGS1ZMKYiEOXhGAYj12vAL0AKtO4rBLqfHZIl949HognV06kBui2kF32CL4JtzkK95kcizeRRmZcjV4HsH7SEeN4OEuCqlirelkzNMIX3v0nkh0hokmappAlwxqGWT9rYCWU8Xo/QDPny0BnszXwioR5ApYCOwmbEAwAmQE2EzTLoVGq8ay5mN+X+X7mcDRfUnTuu0QlJ6GuTxdAS9rJVL3YqAvPF+jeuzGrG1p3lVrLTS3zC+S/URNkQFYo82Zr1u1AI55ozJJEvOFYZSYXJtXi/u4mTf9Ap+NRTYpMNOOlrS1lftmokuESvbS9c9u7rWwgP7PEpaPhfayXOfSEUvgKm+vmBpJgCaXQ+XX6sasazRXxbMW6/qnxVEVbTGVPtUN2Gtvh9pb5xaQQL6k/artKkC1wfjuNme4Zr6OEa0AblXXEoAi74XeC36qRkqacANaplCpdareSpG9cYCXNcgQlCdLAgQtulOXzUpC7zAofGxtKPhewxPAnJkvNwF2a+aG/aqVxMt5dgCfcteuy7bY0wwA9okBZc+BBx0A3oF0V5jUbqI5btGR3NEkYG05b7Tm4B27VoDWk/koUQDvNE0OPfsKmpruSF5j6VU51Kz5cqNltYEKPduzWbjwVALcZnOBKjbgC3D2Sg9tdwS9w/Y7fvGSec6aubRGqatLYmzx6owbTl7RenaorAbPM6eu+ksau1d6gvrkIGiKXurQKXIldz+1kBw1HNeFWq+JlXY3dE4L2nuY9QH7HvHlHhlyR3M3/FZMIMO6lU3cQZ/YnY4APToY+9PIou/Hic0jVTZmg9ZMnx009QmkobV8EHgmrxr3yXUtd1yAtcqTkw+mTzAVmKv36QFl7oFNfMRxYrcBNLrYkls6vQv/9VrTXg4+QIEG2gpHn+/Is9V70N0A93zwpHJJnxk+7qdFvoGmBwCOBDxR44XD4ZL7jBZzF4NTE3gPE7f6iC/PHPbc5OLpWZq6ZbD4/Ltn1AUGwxP8dMqAPnXN7KmX9hYLH1egVbz3OabBNU2bg7ln93DFHjS+UoBtwDWBm22gCQz/ewaXa+eTw5mAgR267DQuf9SUUlUx1lcwf60tbZEqRC8pEgqNf6xr+TUEpoTx/0JLrdOUlaatwL8uaXlPjUUjdAm8FNJa0HzhffoPEnOtV2bGLL/H9/ITtPtaf9r+E2AA4bfLT+prOiQAAAAASUVORK5CYII=)"
            }
          : {
              left: `${x}px`,
              top: `${y}px`
            }

        return style
      }

      function infoStyle(part: string) {
        let x = 28
        let y = 5
        let index = display_parts.findIndex(p => p == part)
        let type = characterStore.getForge(part, "cursed_type")

        if (index == 13) index -= 7
        else if (index >= 5 && index <= 12) {
          x += 189
          index -= 5
        }

        x += (index % 2) * 32
        y += Math.floor(index / 2) * 32

        let style = {
          left: `${x}px`,
          top: `${y}px`,
          zIndex: 4,
          color: type ? "#19C7EA" : "#E458A9",
          fontWeight: "bolder"
        }

        return style
      }

      function currentInfo(part: string) {
        let num = characterStore.getForge(part, "cursed_number")
        return num ? "+" + num : ""
      }

      function setPart(part: string) {
        return () => {
          // activeIndex.value = index
          detailsStore.setPart(part)
        }
      }

      return () => (
        <div class="pro-char-info">
          <div class="head" style="background-image:url(images/common/head.png)">
            <div class="w-266px h-170px bg-bottom flex char" style={"background-image:url(images/characters/" + characterStore.alter + "/人物.png);background-repeat: no-repeat; position: absolute;"}>
              [{characterStore.name}]
              {renderList(display_parts, (item, index) => (
                <>
                  <div onClick={setPart(item)} class="absolute w-7 h-7" style={infoStyle(item)}>
                    {currentInfo(item)}
                  </div>
                  <div onClick={setPart(item)} class="absolute w-7 h-7" style={partIconStyle(item)}></div>
                </>
              ))}
            </div>
            <div class="h-150px w-266px" style="background-image:url(images/common/equ-back.png)"></div>
          </div>
        </div>
      )
    }
  })
</script>
<style lang="scss">
  .pro-char-info {
    width: 266px;
    height: 180px;
    position: relative;
    padding: 5px;
    font-size: 12px;

    // background-color: rgba(255, 255, 255, 0.5);
    // background-image: url("./img/60.png");
    .head {
      background-repeat: no-repeat;
      height: 177px;
      display: flex;
      justify-content: center;
      border: 1px solid rgba(255, 255, 255, 0.1);
      .char {
        display: flex;
        justify-content: center;
        align-items: flex-end;
        color: white;
      }
    }
  }
</style>
