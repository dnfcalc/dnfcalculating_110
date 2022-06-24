<script lang="tsx">
  import { IEquipmentInfo } from "@/api/info/type"
  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
  import { useCharacterStore, useConfigStore, useDetailsStore } from "@/store"
  import { to_percent } from "@/utils"
  import { computed, defineComponent, PropType, renderList } from "vue"

  interface DelearProperties {
    技能攻击力: number
    攻击强化: number
    百分比攻击强化: number
    MP消耗量: number
    伤害比例: number[]
    伤害系数: number[]
    无色消耗: number
  }

  interface BufferProperties {
    buffer_power: number
    buffer_power_value: number
    buffer_power_per: number
    buff_name: string
    buff_level: number
    awake_name: string
    awake_level: number
  }

  interface IDetail {
    name?: string
    alter?: string

    fame?: number

    站街?: {
      智力?: number
      力量?: number
      物理攻击?: number
      魔法攻击?: number
      独立攻击?: number
      火?: number
      冰?: number
      光?: number
      暗?: number
    }
    jintu?: {
      智力?: number
      力量?: number
      物理攻击?: number
      魔法攻击?: number
      独立攻击?: number
      火?: number
      冰?: number
      光?: number
      暗?: number
    }
    properties?: DelearProperties & BufferProperties
    buffer_addition: [number, number, number, number]
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
    name: "profile",
    props: {
      charName: {
        type: String,
        default: null
      },
      details: {
        type: Object as PropType<IDetail>,
        default: () => {
          return {
            fame: 0,
            站街: { 火: 0, 冰: 0, 光: 0, 暗: 0 },
            role: "delear",
            properties: {
              技能攻击力: 0,
              攻击强化: 0,
              百分比攻击强化: 0,
              MP消耗量: 0,
              伤害比例: [1, 0, 0, 0, 0],
              伤害系数: [1, 1, 1, 1, 1]
            },
            buffer_addition: [0, 0, 0, 0]
          }
        }
      },
      role: {
        type: String as PropType<"delear" | "buffer">,
        default: () => "delear"
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
      totalData: {
        type: Array as PropType<number[]>,
        default: () => {
          return [0]
        }
      },
      standardSum: {
        type: Number
      }
    },
    components: { EquipTips },
    setup(props, { emit }) {
      // let details = props.details as IDetail

      const details = computed(() => (props.details as IDetail) ?? undefined)
      // details.站街 = {
      //   火: 999,
      //   冰: 999,
      //   光: 999,
      //   an: 999
      // }

      const current_data = computed(() => props.totalData?.[0] ?? 0)

      console.log(props.role)

      const result = computed(() => {
        const total_data = current_data.value
        if (total_data) {
          if (props.standardSum) {
            if (total_data == props.standardSum) {
              return ["无变化", "white"]
            } else {
              return [to_percent(total_data / props.standardSum - 1, 0, "%", true), total_data > props.standardSum ? "#3ea74e" : "red"]
            }
          }
          if (props.role == "buffer") {
            console.log(total_data, to_percent(total_data, 0, "%", true))
            return [to_percent(total_data / 100, 0, "%", true), "green"]
          }
          return [total_data.round(0).toLocaleString(), "white"]
        }
        return [" -- ", "white"]
      })

      const configStore = useConfigStore()
      const characterStore = useCharacterStore()
      const detailsStore = useDetailsStore()
      // const basicStore = useBasicInfoStore()
      const display_parts = detailsStore.display_parts

      function currentInfo(part: string) {
        if (["称号", "宠物"].indexOf(part) >= 0) return ""
        let num = configStore.getForge(part, "cursed_number") ?? 0
        if (getEqu(part)?.type == "智慧产物") {
          num = configStore.getForge(part, "wisdom_number") ?? 0
        }
        return "+" + num
      }

      function infoStyle(part: string) {
        let x = 28
        let y = 5
        let index = display_parts.findIndex(p => p == part)
        let type = configStore.getForge(part, "cursed_type")
        if (getEqu(part)?.type == "智慧产物") {
          type = 3
        }
        if (index == 13) index -= 7
        else if (index >= 5 && index <= 12) {
          x += 179
          index -= 5
        }

        x += (index % 2) * 39
        y += Math.floor(index / 2) * 34

        let style = {
          left: `${x}px`,
          top: `${y}px`,
          zIndex: 4,
          color: type == 2 ? "#19C7EA" : type == 3 ? "orange" : "#E458A9",
          fontWeight: 900,
          backgroundColor: "rgba(0,0,0,0.5)"
        }

        return style
      }

      function partIconStyle(part: string) {
        let x = 11
        let y = 11
        let index = display_parts.findIndex(p => p == part)
        let active = index == display_parts.findIndex(p => p == detailsStore.part)

        if (index == 13) index -= 7
        else if (index >= 5 && index <= 12) {
          x += 179
          index -= 5
        }

        x += (index % 2) * 39
        y += Math.floor(index / 2) * 34

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
        return props.equList.filter(item => item.typeName == part)[0] ?? undefined
      }

      function renderDelearPropties() {
        const properties = details.value?.properties
        const town = details.value?.站街
        if (!properties || !town) {
          return []
        }
        return (
          <>
            <div class="details">
              {town.力量 && (
                <div class="de-item">
                  <img class="h-15px w-15px" src={"./images/common/icon/" + ICONS.力量 + ".png"} />
                  <div class="text-hex-836832 name">力量</div>
                  <div class="text-hex-3ea74e">{details.value?.站街?.力量?.toFixed(0)}</div>
                </div>
              )}
              {town.智力 && (
                <div class="de-item">
                  <div class="flex items-center">
                    <img class="h-15px w-15px" src={"./images/common/icon/" + ICONS.智力 + ".png"} />
                    <div class="text-hex-836832 name">智力</div>
                  </div>
                  <div class="text-hex-3ea74e">{details.value?.站街?.智力?.toFixed(0)}</div>
                </div>
              )}

              {town.物理攻击 && (
                <div class="de-item">
                  <div class="flex items-center">
                    <img class="h-15px w-15px" src={"./images/common/icon/" + ICONS.物理攻击 + ".png"} />
                    <div class="text-hex-836832 name">物理攻击</div>
                  </div>
                  <div class="text-hex-3ea74e">{details.value?.站街?.物理攻击?.toFixed(0)}</div>
                </div>
              )}

              {town.魔法攻击 && (
                <div class="de-item">
                  <div class="flex items-center">
                    <img class="h-15px w-15px" src={"./images/common/icon/" + ICONS.魔法攻击 + ".png"} />
                    <div class="text-hex-836832 name">魔法攻击</div>
                  </div>
                  <div class="text-hex-3ea74e">{details.value?.站街?.魔法攻击?.toFixed(0)}</div>
                </div>
              )}

              {town.独立攻击 && (
                <div class="de-item">
                  <div class="flex items-center">
                    <img class="h-15px" src={"./images/common/icon/" + ICONS.独立攻击 + ".png"} />
                    <div class="text-hex-836832 name">独立攻击</div>
                  </div>
                  <div class="text-hex-3ea74e">{details.value?.站街?.独立攻击?.toFixed(0)}</div>
                </div>
              )}

              <div class="de-item">
                <div class="flex items-center">
                  <img class="h-15px w-15px" src={"./images/common/icon/" + ICONS.攻击属性 + ".png"} />
                  <div class="text-hex-836832 name">攻击属性</div>
                </div>
                <div class="text-hex-3ea74e">{`火(${details.value?.站街?.火?.toFixed(0)})/冰(${details.value?.站街?.冰?.toFixed(0)})/光(${details.value?.站街?.光?.toFixed(
                  0
                )})/暗(${details.value?.站街?.暗?.toFixed(0)})`}</div>
              </div>
            </div>
            <div class="details">
              <div class="de-item">
                <div class="text-hex-836832">技能攻击力</div>
                <div class="text-hex-3ea74e">{properties.技能攻击力.toFixed(2) + "%"}</div>
              </div>
              <div class="de-item">
                <div class=" text-hex-836832">直伤</div>
                <div class="text-hex-3ea74e">{`${(properties.伤害比例?.[0] ?? 1).round(2) * 100}%`}</div>
              </div>
              <div class="de-item">
                <div class=" text-hex-836832">攻击强化</div>
                <div class="text-hex-3ea74e">{properties.攻击强化?.round(0)}</div>
              </div>
              <div class="de-item">
                <div class=" text-hex-836832">攻击强化%</div>
                <div class="text-hex-3ea74e">{properties.百分比攻击强化?.toFixed(2) + "%"}</div>
              </div>
              <div class="de-item">
                <div class=" text-hex-836832">无色消耗</div>
                <div class="text-hex-3ea74e">{properties.无色消耗}</div>
              </div>
              <div class="de-item">
                <div class=" text-hex-836832">MP消耗量%</div>
                <div class="text-hex-3ea74e">{properties.MP消耗量?.toFixed(2) + "%"}</div>
              </div>
              <div class="de-item">
                <div class=" text-hex-836832">中毒</div>
                <div class="text-hex-3ea74e">{`${(properties.伤害比例?.[1] ?? 0) * 100}%(+${((properties.伤害系数?.[1] ?? 0).round(2) * 100).toFixed(0)}%)`}</div>
              </div>
              <div class="de-item">
                <div class=" text-hex-836832">灼烧</div>
                <div class="text-hex-3ea74e">{`${(properties.伤害比例?.[2] ?? 0) * 100}%(+${((properties.伤害系数?.[2] ?? 0).round(2) * 100).toFixed(0)}%)`}</div>
              </div>
              <div class="de-item">
                <div class=" text-hex-836832">感电</div>
                <div class="text-hex-3ea74e">{`${(properties.伤害比例?.[3] ?? 0) * 100}%(+${((properties.伤害系数?.[3] ?? 0).round(2) * 100).toFixed(0)}%)`}</div>
              </div>
              <div class="de-item">
                <div class=" text-hex-836832">出血</div>
                <div class="text-hex-3ea74e">{`${(properties.伤害比例?.[4] ?? 0) * 100}%(+${((properties.伤害系数?.[4] ?? 0).round(2) * 100).toFixed(0)}%)`}</div>
              </div>
            </div>
          </>
        )
      }

      function renderBufferProperties() {
        if (!details.value) {
          return []
        }
        const properties = details.value?.properties
        const town = details.value.站街
        if (!properties || !town) {
          return []
        }
        return (
          <>
            <div class="details">
              {town.智力 && (
                <div class="de-item">
                  <div class="flex items-center">
                    <img class="h-15px w-15px" src={"./images/common/icon/" + ICONS.智力 + ".png"} />
                    <div class="text-hex-836832 name">智力</div>
                  </div>
                  <div class="text-hex-3ea74e">{town.智力?.toFixed(0)}</div>
                </div>
              )}
              <calc-tooltip class="de-item" position="bottom">
                {{
                  default() {
                    return (
                      <>
                        <div class="text-hex-836832">BUFF量</div>
                        <div class="text-hex-3ea74e">{properties.buffer_power?.round(0)}</div>
                      </>
                    )
                  },
                  popper() {
                    return <div class="text-white py-1 px-2">{`BUFF量:${properties.buffer_power_value}(+${properties.buffer_power_per}%)`}</div>
                  }
                }}
              </calc-tooltip>
              <calc-tooltip position="bottom" class="de-item">
                {{
                  default() {
                    return (
                      <>
                        <div class=" text-hex-836832">Buff技能等级</div>
                        <div class="text-hex-3ea74e">{properties.buff_level}</div>
                      </>
                    )
                  }
                  // popper() {
                  //   return (
                  //     <div class="text-white py-1 px-2">
                  //       <div>{`${properties.buff_name} Lv.${properties.buff_level}`}</div>
                  //     </div>
                  //   )
                  // }
                }}
              </calc-tooltip>
              <calc-tooltip position="bottom" class="de-item">
                {{
                  default() {
                    return (
                      <>
                        <div class=" text-hex-836832">觉醒技能等级</div>
                        <div class="text-hex-3ea74e">{properties.awake_level}</div>
                      </>
                    )
                  }
                }}
              </calc-tooltip>
              <div class="de-item">
                <div class=" text-hex-836832">力智加成</div>
                <div class="text-hex-3ea74e">{props.totalData[2]?.round(0)}</div>
              </div>
              <div class="de-item">
                <div class=" text-hex-836832">三攻加成</div>
                <div class="text-hex-3ea74e">{props.totalData[3]?.round(0)}</div>
              </div>
            </div>
          </>
        )
      }

      return () => {
        return (
          <div class="char-info">
            <div class="char-back">
              <div class="head" style="background-image:url(./images/common/head.png)">
                <div
                  class="bg-bottom flex h-170px w-266px char"
                  style={"background-image:url(./images/characters/" + characterStore.alter + "/profile.png);background-repeat: no-repeat; position: absolute;"}
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
                <div class="h-150px w-266px" style="background-image:url(./images/common/equ-back.png)"></div>
              </div>
              {props.showDetail && (
                <>
                  {props.showMW && (
                    <div class="fame">
                      <img src="./images/common/fame.png" />
                      <div class="ml-2px text-hex-836832">冒险家名望</div>
                      <div class="ml-8px text-hex-3ea74e" style="width:55px">
                        {details.value?.fame}
                      </div>
                    </div>
                  )}
                  {props.role == "delear" ? renderDelearPropties() : renderBufferProperties()}

                  {
                    <div class="sum" style={"color:" + result.value[1]}>
                      {result.value[0]}
                    </div>
                  }
                </>
              )}
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

      .fame {
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
        display: flex;
        flex-wrap: wrap;

        -webkit-font-smoothing: none;
        // background-color: rgba(0, 0, 0, 0.8);
        margin-top: 2px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        .de-item {
          height: 20px;
          display: flex;
          justify-content: space-between;
          align-items: center;
          min-width: 50%;
          padding: 0 5px;
          box-sizing: border-box;
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
        font-size: 25px;
      }
    }
  }
</style>
