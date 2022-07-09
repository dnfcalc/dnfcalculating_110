<script lang="tsx">
  import { IEquipmentInfo } from "@/api/info/type"
  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
  import EquipIcon from "@/components/internal/equip/eq-icon.vue"
  import { useBasicInfoStore, useCharacterStore, useConfigStore, useDetailsStore } from "@/store"
  import { to_percent } from "@/utils"
  import { useVModel } from "@vueuse/core"
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
    apply_value: number
  }

  interface IDetail {
    name?: string
    alter?: string

    fame?: number

    站街?: {
      智力?: number
      力量?: number
      体力?: number
      精神?: number
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
      standardData: {
        type: Array as PropType<number[]>,
        default: () => {
          return [0]
        }
      },
      equips_forget: {
        type: Object,
        default: undefined
      },
      part: {
        type: String,
        default: ""
      }
    },
    components: { EquipTips },
    setup(props, { emit }) {
      const partModelValue = useVModel(props, "part", emit, { passive: true })
      // let details = props.details as IDetail

      const details = computed(() => (props.details as IDetail) ?? undefined)
      // details.站街 = {
      //   火: 999,
      //   冰: 999,
      //   光: 999,
      //   an: 999
      // }

      const current_data = computed(() => props.totalData?.[0] ?? 0)
      const standard_data = computed(() => props.standardData?.[0] ?? 0)

      const result = computed(() => {
        const current = current_data.value
        const standard = standard_data.value

        if (!!current) {
          if (!!standard) {
            if (current == standard) {
              return ["无变化", "white"]
            } else {
              return [to_percent(current / standard - 1, 0, "%", true), current > standard ? "#3ea74e" : "red"]
            }
          }
          if (props.role == "buffer") {
            return [to_percent(current / 100, 0, "%", true), "green"]
          }
          return [current.round(0).toLocaleString(), "white"]
        }
        return [" -- ", "white"]
      })

      const configStore = useConfigStore()
      const characterStore = useCharacterStore()
      const detailsStore = useDetailsStore()
      const basicStore = useBasicInfoStore()
      const display_parts = detailsStore.display_parts

      const equips_forget = function (index: string) {
        // console.log(props.equips_forget)
        let infos = configStore.forge_set[index]
        if (!infos) return undefined
        return {
          info: {
            成长词条等级: [infos.get("growth_first") ?? 1, infos.get("growth_second") ?? 1, infos.get("growth_third") ?? 1, infos.get("growth_fourth") ?? 1],
            // 1增幅 2强化
            强化类型: infos.get("cursed_type") ?? 1,
            强化数值: infos.get("cursed_number") ?? 0,
            锻造数值: infos.get("dz_number") ?? 0,
            附魔: basicStore.details.enchanting?.filter(item => item.id == infos.get("enchanting") ?? 0)?.[0]?.props?.split("|"),
            徽章: [
              basicStore.details.emblem?.filter(item => item.id == infos.get("socket_left") ?? 0)?.[0]?.props,
              basicStore.details.emblem?.filter(item => item.id == infos.get("socket_right") ?? 0)?.[0]?.props
            ]
          },
          data: props.equips_forget?.[index]
        }
      }

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

        if (index == 13) {
          index -= 7
        } else if (index >= 5 && index <= 12) {
          x += 179
          index -= 5
        }

        x += (index % 2) * 39
        y += Math.floor(index / 2) * 34

        return {
          left: `${x}px`,
          top: `${y}px`
        }
      }

      function setPart(part: string) {
        return () => {
          // activeIndex.value = index
          partModelValue.value = part
          emit("partChange", part)
        }
      }

      function getEqu(part: string) {
        return props.equList.filter(item => item.part == part)[0] ?? undefined
      }

      function getEquCustom(part: string) {
        const id = (props.equList.filter(item => item.part == part)[0] ?? undefined).id
        if (id) {
          const customs = configStore.customize[id.toString()]
          let temp: any = []
          customs?.forEach(index => {
            temp.push(basicStore.entry_list?.[index.toString()])
          })
          // console.log(temp)
          return temp
        } else return []
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
                <div class="de-item !pl-0 ">
                  <div class="flex items-center">
                    <img class="h-15px w-15px" src={"/images/common/icon/" + ICONS.力量 + ".png"} />
                    <div class="text-hex-836832 name">力量</div>
                  </div>
                  <div class="text-hex-3ea74e">{details.value?.站街?.力量?.toFixed(0)}</div>
                </div>
              )}
              {town.智力 && (
                <div class="de-item  !pl-0">
                  <div class="flex items-center">
                    <img class="h-15px w-15px" src={"/images/common/icon/" + ICONS.智力 + ".png"} />
                    <div class="text-hex-836832 name">智力</div>
                  </div>
                  <div class="text-hex-3ea74e">{details.value?.站街?.智力?.toFixed(0)}</div>
                </div>
              )}

              {town.物理攻击 && (
                <div class="de-item  !pl-0">
                  <div class="flex items-center">
                    <img class="h-15px w-15px" src={"/images/common/icon/" + ICONS.物理攻击 + ".png"} />
                    <div class="text-hex-836832 name">物理攻击</div>
                  </div>
                  <div class="text-hex-3ea74e">{details.value?.站街?.物理攻击?.toFixed(0)}</div>
                </div>
              )}

              {town.魔法攻击 && (
                <div class="de-item  !pl-0">
                  <div class="flex items-center">
                    <img class="h-15px w-15px" src={"/images/common/icon/" + ICONS.魔法攻击 + ".png"} />
                    <div class="text-hex-836832 name">魔法攻击</div>
                  </div>
                  <div class="text-hex-3ea74e">{details.value?.站街?.魔法攻击?.toFixed(0)}</div>
                </div>
              )}

              {town.独立攻击 && (
                <div class="de-item  !pl-0">
                  <div class="flex items-center">
                    <img class="h-15px" src={"/images/common/icon/" + ICONS.独立攻击 + ".png"} />
                    <div class="text-hex-836832 name">独立攻击</div>
                  </div>
                  <div class="text-hex-3ea74e">{details.value?.站街?.独立攻击?.toFixed(0)}</div>
                </div>
              )}

              <div class="w-100% de-item !pl-0">
                <div class="flex items-center">
                  <img class="h-15px w-15px" src={"/images/common/icon/" + ICONS.攻击属性 + ".png"} />
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
              <calc-tooltip class="de-item" position="bottom">
                {{
                  default() {
                    return (
                      <>
                        <div class="text-hex-836832">攻击强化</div>
                        <div class="text-hex-3ea74e">{(((properties.攻击强化 ?? 0) * (100 + properties.百分比攻击强化 ?? 0)) / 100).toFixed(0)}</div>
                      </>
                    )
                  },
                  popper() {
                    return <div class="text-white py-1 px-2">{`攻击强化:${properties.攻击强化}(+${properties.百分比攻击强化?.toFixed(2)}%)`}</div>
                  }
                }}
              </calc-tooltip>
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

        let coreProperty: JSX.Element

        if (town.智力) {
        }

        return (
          <>
            <div class="details">
              {town.智力 && (
                <calc-tooltip class="de-item" position="bottom">
                  {{
                    default() {
                      return (
                        <>
                          <div class="flex items-center">
                            <img class="h-15px w-15px" src={"/images/common/icon/" + ICONS.智力 + ".png"} />
                            <div class="text-hex-836832 name">智力</div>
                          </div>
                          <div class="text-hex-3ea74e">{town.智力?.toFixed(0)}</div>
                        </>
                      )
                    },
                    popper() {
                      return <div class="text-white py-1 px-2">{`适用数值:${properties.apply_value}`}</div>
                    }
                  }}
                </calc-tooltip>
              )}

              {town.体力 && (
                <calc-tooltip class="de-item" position="bottom">
                  {{
                    default() {
                      return (
                        <>
                          <div class="flex items-center">
                            <img class="h-15px w-15px" src={"/images/common/icon/" + ICONS.体力 + ".png"} />
                            <div class="text-hex-836832 name">体力</div>
                          </div>
                          <div class="text-hex-3ea74e">{town.体力?.toFixed(0)}</div>
                        </>
                      )
                    },
                    popper() {
                      return <div class="text-white py-1 px-2">{`适用数值:${properties.apply_value}`}</div>
                    }
                  }}
                </calc-tooltip>
              )}

              {town.精神 && (
                <calc-tooltip class="de-item" position="bottom">
                  {{
                    default() {
                      return (
                        <>
                          <div class="flex items-center">
                            <img class="h-15px w-15px" src={"/images/common/icon/" + ICONS.精神 + ".png"} />
                            <div class="text-hex-836832 name">精神</div>
                          </div>
                          <div class="text-hex-3ea74e">{town.精神?.toFixed(0)}</div>
                        </>
                      )
                    },
                    popper() {
                      return <div class="text-white py-1 px-2">{`适用数值:${properties.apply_value}`}</div>
                    }
                  }}
                </calc-tooltip>
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
              <div class="head" style="background-image:url(/images/common/head.png)">
                <div
                  class="bg-bottom flex h-170px w-266px char"
                  style={"background-image:url(/images/characters/" + characterStore.alter + "/profile.png);background-repeat: no-repeat; position: absolute;"}
                >
                  [{characterStore.name}]
                  {renderList(display_parts, (part, index) => (
                    <>
                      <div onClick={setPart(part)} class="absolute" style={infoStyle(part)}>
                        {currentInfo(part)}
                      </div>
                      <div onClick={setPart(part)} class="absolute " style={partIconStyle(part)}>
                        <div class="h-full w-full relative overflow-hidden">
                          {getEqu(part) ? (
                            <EquipTips
                              hightlight={part == partModelValue.value}
                              class="h-full w-full"
                              forget={equips_forget(part)}
                              eq={getEqu(part)}
                              pps={getEquCustom(part)}
                              canClick={false}
                              show-tips
                            ></EquipTips>
                          ) : (
                            <EquipIcon hightlight={part == partModelValue.value} />
                          )}
                        </div>
                      </div>
                    </>
                  ))}
                </div>
                <div class="h-150px w-266px" style="background-image:url(/images/common/equ-back.png)"></div>
              </div>
              {props.showDetail && (
                <>
                  {props.showMW && (
                    <div class="fame">
                      <img src="/images/common/fame.png" />
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
            padding-right: 3px;
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

      .equ-mask {
        background-image: url("@/assets/img/item_hover.png");
        background-repeat: no-repeat;
        background-size: 100% 100%;
      }
    }
  }
</style>
