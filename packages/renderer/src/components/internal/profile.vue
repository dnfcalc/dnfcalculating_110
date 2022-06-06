<script lang="tsx">
  import { IEquipmentInfo } from "@/api/info/type"
  import { useCharacterStore, useDetailsStore, useConfigStore } from "@/store"
  import { computed, defineComponent, PropType, renderList } from "vue"
  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"

  interface IDetail {
    name?: string
    alter?: string

    mingwang?: number
    zhanjie?: {
      zhili?: number
      liliang?: number
      wuligongji?: number
      mofagongji?: number
      duligongji?: number
      huo?: number
      bing?: number
      guang?: number
      an?: number
    }
    jintu?: {
      zhili?: number
      liliang?: number
      wuligongji?: number
      mofagongji?: number
      duligongji?: number
      huo?: number
      bing?: number
      guang?: number
      an?: number
    }
  }

  enum ICONS {
    "力量",
    "智力",
    "物理攻击",
    "魔法攻击",
    "物理暴击",
    "魔法暴击",
    "攻击速度",
    "施放速度",
    "移动速度",
    "命中率",
    "独立攻击",
    "攻击属性",
    "体力",
    "精神"
  }

  export default defineComponent({
    name: "char-info",
    props: {
      eq: {
        type: Object,
        default: () => {}
      },
      charName: {
        type: String,
        default: null
      },
      charType: {
        type: String,
        default: "魔法固伤"
      },
      details: {
        type: Object,
        default: () => {
          return { mingwang: 0, zhanjie: { huo: 0, bing: 0, guang: 0, an: 0 }, jintu: { huo: 0, bing: 0, guang: 0, an: 0 } }
        }
      },
      canChoose: {
        type: Boolean,
        default: false
      },
      showDetail: {
        type: Boolean,
        default: true
      },
      showMW: {
        type: Boolean,
        default: false
      },
      equList: {
        type: Array as PropType<IEquipmentInfo[]>,
        default: []
      },
      sumdamage: {
        type: Number
      }
    },
    components: { EquipTips },
    setup(props, { emit }) {
      // let details = props.details as IDetail

      const details = computed(() => (props.details as IDetail) ?? undefined)
      // details.zhanjie = {
      //   huo: 999,
      //   bing: 999,
      //   guang: 999,
      //   an: 999
      // }

      const configStore = useConfigStore()
      const characterStore = useCharacterStore()
      const detailsStore = useDetailsStore()
      const display_parts = detailsStore.display_parts

      function currentInfo(part: string) {
        let num = configStore.getForge(part, "cursed_number")
        return num ? "+" + num : ""
      }

      function infoStyle(part: string) {
        let x = 28
        let y = 5
        let index = display_parts.findIndex(p => p == part)
        let type = configStore.getForge(part, "cursed_type")

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
          color: type == 2 ? "#19C7EA" : "#E458A9",
          fontWeight: 900,
          backgroundColor: "rgba(0,0,0,0.5)"
        }

        return style
      }

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

        let style =
          active && props.canChoose
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

      function setPart(part: string) {
        return () => {
          // activeIndex.value = index
          detailsStore.setPart(part)
        }
      }

      function getEqu(part: string) {
        return props.equList.filter(item => item.typeName == part)[0] || undefined
      }

      return () => {
        return (
          <div class="char-info">
            <div class="char-back">
              <div class="head" style="background-image:url(images/common/head.png)">
                <div
                  class="bg-bottom flex h-170px w-266px char"
                  style={"background-image:url(images/characters/" + characterStore.alter + "/profile.png);background-repeat: no-repeat; position: absolute;"}
                >
                  [{characterStore.name}]
                  {renderList(display_parts, (item, index) => (
                    <>
                      <div onClick={setPart(item)} class="absolute" style={infoStyle(item)}>
                        {currentInfo(item)}
                      </div>
                      <div onClick={setPart(item)} class="h-7 w-7 absolute" style={partIconStyle(item)}>
                        {getEqu(item) && <EquipTips eq={getEqu(item)} canClick={false} show-tips></EquipTips>}
                      </div>
                    </>
                  ))}
                </div>
                <div class="h-150px w-266px" style="background-image:url(images/common/equ-back.png)"></div>
              </div>
              {props.showDetail && (
                <>
                  {props.showMW && (
                    <div class="mingwang">
                      <img src="./images/common/mingwang.png" />
                      <div class="ml-2px text-hex-836832">冒险家名望</div>
                      <div class="ml-8px text-hex-3ea74e" style="width:55px">
                        {details.value?.mingwang}
                      </div>
                    </div>
                  )}
                  <div class="details">
                    <div class="de-item">
                      <img class="h-15px w-15px" src={"./images/common/icon/" + ICONS.力量 + ".png"} />
                      <div class="text-hex-836832 name">力量</div>
                      <div class="text-hex-3ea74e">{details.value?.zhanjie?.liliang?.toFixed(0)}</div>
                    </div>
                    <div class="de-item">
                      <img class="h-15px w-15px" src={"./images/common/icon/" + ICONS.智力 + ".png"} />
                      <div class="text-hex-836832 name">智力</div>
                      <div class="text-hex-3ea74e">{details.value?.zhanjie?.zhili?.toFixed(0)}</div>
                    </div>

                    <div class="de-item">
                      <img class="h-15px w-15px" src={"./images/common/icon/" + ICONS.物理攻击 + ".png"} />
                      <div class="text-hex-836832 name">物理攻击</div>
                      <div class="text-hex-3ea74e">{details.value?.zhanjie?.wuligongji?.toFixed(0)}</div>
                    </div>

                    <div class="de-item">
                      <img class="h-15px w-15px" src={"./images/common/icon/" + ICONS.魔法攻击 + ".png"} />
                      <div class="text-hex-836832 name">魔法攻击</div>
                      <div class="text-hex-3ea74e">{details.value?.zhanjie?.mofagongji?.toFixed(0)}</div>
                    </div>

                    <div class="de-item">
                      <img class="h-15px w-15px" src={"./images/common/icon/" + ICONS.独立攻击 + ".png"} />
                      <div class="text-hex-836832 name">独立攻击</div>
                      <div class="text-hex-3ea74e">{details.value?.zhanjie?.duligongji?.toFixed(0)}</div>
                    </div>

                    <div class="de-item">
                      <img class="h-15px w-15px" src={"./images/common/icon/" + ICONS.攻击属性 + ".png"} />
                      <div class="text-hex-836832 name">攻击属性</div>
                      <div class="text-hex-3ea74e">{`火(${details.value?.zhanjie?.huo?.toFixed(0)})/冰(${details.value?.zhanjie?.bing?.toFixed(0)})/光(${details.value?.zhanjie?.guang?.toFixed(
                        0
                      )})/暗(${details.value?.zhanjie?.an?.toFixed(0)})`}</div>
                    </div>
                  </div>
                </>
              )}
              {<div class="sum">{props.sumdamage != undefined ? props.sumdamage.round(0).toLocaleString() : "- -"}</div>}
            </div>
          </div>
        )
      }
    }
  })
</script>
<style lang="scss">
  .char-info {
    width: 266px;
    position: relative;
    padding: 5px;
    // margin: 5px;
    // font-size: 12px;
    // background-color: rgba(0, 0, 0, 0.8);

    // background-color: rgba(255, 255, 255, 0.5);
    // background-image: url("./img/60.png");

    .char-back {
      background-color: rgba(0, 0, 0, 0.75);
      border-left: 1px solid rgba(255, 255, 255, 0.1);
      border-right: 1px solid rgba(255, 255, 255, 0.1);
      .head {
        background-repeat: no-repeat;
        height: 177px;
        display: flex;
        justify-content: center;
        // background-color: rgba(0, 0, 0, 0.8);
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        .char {
          display: flex;
          justify-content: center;
          align-items: flex-end;
          color: white;
        }
      }

      .mingwang {
        height: 25px;
        // background-color: rgba(0, 0, 0, 0.8);
        margin-top: 2px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        justify-content: center;
        align-items: center;
      }

      .details {
        max-height: 160px;
        overflow-y: auto;
        padding-top: 5px;
        padding-bottom: 5px;

        -webkit-font-smoothing: none;
        // background-color: rgba(0, 0, 0, 0.8);
        margin-top: 2px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        .de-item {
          height: 20px;
          display: flex;
          align-items: center;
          img {
            padding-left: 5px;
            padding-right: 5px;
            width: 15px;
            height: 15px;
          }

          .name {
            width: 50px;
          }
        }
      }

      .sum {
        height: 50px;
        // border-top: 1px solid rgba(255, 255, 255, 0.1);
        // border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        border-top: 1px solid;
        border-image-source: linear-gradient(to right, #644f23, #d8b04f, #644f23);
        margin-left: 5px;
        margin-right: 5px;
        border-image-slice: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 25px;
      }
    }
  }
</style>
