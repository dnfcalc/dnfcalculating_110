<script lang="tsx">
  import { useBasicInfoStore, useCharacterStore } from "@/store"
  import { asyncComputed } from "@vueuse/core"
  import { computed, defineComponent, renderList, reactive } from "vue"

  import EqIcon from "./eq-icon.vue"

  interface Status {
    id: number
    label: string
    num: number
    isRate: boolean
    info: string
  }

  interface forBadgeArray {
    type: number
    props: string[]
  }

  type classNames = (id: number) => string | string[] | undefined

  export default defineComponent({
    name: "info-dialog",
    components: { EqIcon },
    props: {
      eid: {
        type: Number
      },
      simple: {
        type: Boolean,
        default: false
      },
      colums: {
        type: Boolean,
        default: false
      },
      star: {
        type: Boolean,
        default: false
      },
      isStar: {
        type: Boolean,
        default: false
      },
      forget: {
        type: Object,
        default: () => {}
      },
      pps: {
        type: Array,
        default: () => []
      },
      withTransform: {
        type: Boolean,
        default: true
      }
    },
    setup(props, { emit, slots }) {
      const basicStore = useBasicInfoStore()

      const equip = asyncComputed(async () => {
        if (props.eid != undefined) {
          let temp = await basicStore.get_equipment_detail(props.eid)
          if (props.withTransform) {
            loadTransform(temp) // 加载打造数据
          }
          return temp
        }
      })

      function renderStatus(rowClass?: classNames, spanClass?: classNames, withTransform?: boolean) {
        return ({ id, label, num, isRate }: Status, indexForStatus: number) => {
          let array: JSX.Element[] = []

          array.push(<span style={num ? "margin-right: 5px" : undefined}>{label}</span>)
          const rowClassNames = rowClass?.(id)
          const spanClassNames = spanClass?.(id)
          if (num) {
            let text: any = num
            if (isRate) {
              text = (num * 100).toFixed()
              text = (num > 0 ? "+" : "") + `${text}%`
            }
            //array.push(<span class={spanClassNames}>{text}</span>)
            array.push(<span>{text}</span>)
          }

          let result: JSX.Element = <div class={[rowClassNames]}>{array}</div>
          if (withTransform) {
            let nameIndex = propNames.findIndex(x => x == label)
            if (nameIndex > -1 && (transform.refine > 0 || transform.reinforce > 0)) {
              let arr = setTransform(nameIndex)
              array = array.concat(arr)

              let beforeArr = []
              // 往前查漏补缺
              for (var i = nameIndex - 1; i >= 0; i--) {
                if (isWithTransform(i)) {
                  let name = propNames[i]
                  let index = equip.value.prop.base.findIndex(({ label }: Status) => label == name)
                  if (index >= 0) {
                    console.log(indexForStatus, label, name, "往前， stop")
                    break
                  } else {
                    let tArr = setTransform(i, name)
                    beforeArr.push(<div class={[rowClassNames]}>{tArr}</div>)
                    console.log(indexForStatus, label, name, "往前，find")
                  }
                }
              }
              let arrterArr = []
              // 最后一个， 往后查漏补缺
              if (indexForStatus == equip.value.prop.base.length - 1) {
                for (let i = nameIndex + 1; i < propNames.length; i++) {
                  if (isWithTransform(i)) {
                    let name = propNames[i]
                    let index = equip.value.prop.base.findIndex(({ label }: Status) => label == name)
                    if (index < 0) {
                      let tArr = setTransform(i, name)
                      arrterArr.push(<div class={[rowClassNames]}>{tArr}</div>)

                      console.log(indexForStatus, label, name, "往后，find")
                    }
                  }
                }
              }
              result = (
                <div>
                  {beforeArr}
                  <div class={[rowClassNames]}>{array}</div>
                  {arrterArr}
                </div>
              )
            }
          }
          return result
        }
      }

      function isWithTransform(i: number) {
        return transform.reinforceInfo.strengthen[i] > 0 || transform.reinforceInfo.reinforce[i] > 0 || transform.reinforceInfo.refine[i] > 0
      }

      function setTransform(index: number, name?: string) {
        let array: JSX.Element[] = []
        if (transform.reinforceInfo.strengthen[index] > 0) {
          // 强化
          if (name) {
            array.push(<span class="advanced">{name}</span>)
            array.push(
              <span style="margin-left: 5px" class="advanced">
                {transform.reinforceInfo.strengthen[index]}
              </span>
            )
          } else {
            array.push(
              <span style="margin-left: 5px" class="advanced">
                +{transform.reinforceInfo.strengthen[index]}
              </span>
            )
          }
        }
        if (transform.reinforceInfo.reinforce[index] > 0) {
          // 增幅
          if (name && transform.reinforceInfo.strengthen[index] <= 0) {
            array.push(<span class="artifact">{name}</span>)
            array.push(
              <span style="margin-left: 5px" class="artifact">
                {transform.reinforceInfo.reinforce[index]}
              </span>
            )
          } else {
            array.push(
              <span style="margin-left: 5px" class="artifact">
                +{transform.reinforceInfo.reinforce[index]}
              </span>
            )
          }
        }
        if (transform.reinforceInfo.refine[index] > 0) {
          // 锻造
          if (name && transform.reinforceInfo.strengthen[index] <= 0 && transform.reinforceInfo.reinforce[index] <= 0) {
            array.push(<span class="rare">{name}</span>)
            array.push(
              <span style="margin-left: 5px" class="rare">
                {transform.reinforceInfo.refine[index]}
              </span>
            )
          } else {
            array.push(
              <span style="margin-left: 5px" class="rare">
                +{transform.reinforceInfo.refine[index]}
              </span>
            )
          }
        }
        return array
      }

      const effectClass = function (id: number) {
        if (id > 13) {
          return "strong"
        }
      }

      const growthClass = function (id: number) {
        const classNames = []

        if (id == 100) {
          classNames.push("yellow")
        } else if (id == 102) {
          classNames.push("strong")
        }
        if (id > 100) {
          classNames.push("paddleft")
        }
        if (id >= 1000) {
          classNames.push("suiji-props")
          if (id > 1000) {
            classNames.push("yellow")
          } else {
            classNames.push("gey")
          }
        }
        return classNames
      }

      const characterStore = useCharacterStore()

      const is_buffer = computed(() => characterStore.is_buffer)

      const sum_buffer = computed(() => {
        let s = 0
        if (equip.value?.prop.growthProps && equip.value.prop.growthProps.length > 0) {
          let a = equip.value.prop.growthProps

          for (let i = 0; i < a.length; i++) {
            let item = a[i]
            s += transform.growthBuffers[i] ?? item.buffer ?? 0
          }
        }
        return s
      })

      const sum_attack = computed(() => {
        let s = 0
        if (equip.value?.prop.growthProps && equip.value.prop.growthProps.length > 0) {
          let a = equip.value.prop.growthProps

          for (let i = 0; i < a.length; i++) {
            let item = a[i]
            s += transform.growthAttacks[i] ?? item.attack ?? 0
          }
        }
        return s
      })

      const rarityClass = function (type: string) {
        switch (type) {
          case "史诗":
            return "epic"
          case "神话":
            return "myth"
          case "智慧产物":
            return "epic"
          case "神器":
            return "artifact"
          case "稀有":
            return "rare"
          default:
            return ""
        }
      }

      const propNames = ["力量", "智力", "体力", "精神", "物理攻击力", "魔法攻击力", "独立攻击力"]
      const badgeNames = ["白金徽章镶嵌栏", "红色徽章镶嵌栏", "绿色徽章镶嵌栏", "蓝色徽章镶嵌栏", "黄色徽章镶嵌栏"]
      const badgeClass = ["kong-baijin", "kong-red", "kong-green", "kong-blue", "kong-yellow"]
      const eqBagdes = {
        上衣: 2,
        下装: 2,
        头肩: 4,
        项链: 4,
        腰带: 1,
        戒指: 1,
        鞋: 3,
        手镯: 3,
        辅助装备: 0,
        魔法石: 0
      }

      const transform = reactive({
        enchanting: [] as string[], //["所有属性强化 +30"], // 附魔
        reinforce: 0, // 18, // 增幅、强化数值
        type: 1,
        refine: 0, //8, // 锻造
        reinforceInfo: {
          reinforce: [0, 0, 0, 0, 0, 0, 0], //[0, 91, 91, 0, 0, 0, 0], //增幅
          strengthen: [0, 0, 0, 0, 0, 0, 0], //[29, 29, 0, 29, 0, 0, 0], //强化
          refine: [0, 0, 0, 0, 0, 0, 0], //[0, 0, 0, 0, 0, 0, 539]// 锻造
          refineSW: 0 //[0, 0, 0, 0, 0, 0, 539]// 锻造
        },
        growthLvs: [1, 1, 1, 1], // 词条等级
        growthAttacks: [0, 0, 0, 0], // 词条等级
        growthBuffers: [0, 0, 0, 0], // 词条等级
        badges: [] as forBadgeArray[] //[ { type: 1,  props: [ "智力 +30", ] }, { type: 2,  props: [ "智力+30 魔爆+3%", ] }, { type: 3,  props: [ "物攻 +20", ] },
        //{ type: 4,  props: [ "智力 +15", ] }, { type: 0,  props: [  "四维+8 [冰之领悟]技能Lv+1", ] }, ], // 徽章
      })
      function loadTransform(eq: any) {
        if (props.forget) {
          console.log(props.forget)

          if (props.forget.info) {
            transform.growthLvs = props.forget.info["成长词条等级"] ?? [1, 1, 1, 1]
            transform.growthAttacks = props.forget.data["attack"] ?? [0, 0, 0, 0]
            transform.growthBuffers = props.forget.data["buffer"] ?? [0, 0, 0, 0]
            transform.reinforce = props.forget.info["强化数值"] ?? 0
            transform.refine = props.forget.info["锻造数值"] ?? 0
            transform.enchanting = props.forget.info["附魔"] ?? []

            transform.type = props.forget.info["强化类型"] ?? 1

            // 处理徽章
            transform.badges = []
            if (eq && eq.position) {
              let types = eq.position.split("(")
              let type = types[0]
              let position = type
              if (types.length > 1) {
                position = types[1].split(")")[0]
              }
              let bgs = props.forget.info["徽章"] ?? []
              for (var b of bgs) {
                if (b) {
                  transform.badges.push({
                    type: eqBagdes[position] ?? 0,
                    props: [b]
                  })
                }
              }
            }

            // 处理强化增幅数据
            transform.reinforceInfo.reinforce = [0, 0, 0, 0, 0, 0, 0]
            transform.reinforceInfo.strengthen = [0, 0, 0, 0, 0, 0, 0]
            if (transform.reinforce > 0) {
              if (transform.type == 1 && props.forget.data["增幅四维"] && props.forget.data["增幅四维"].length > 0) {
                // 增幅
                for (var i = 0; i < props.forget.data["增幅四维"].length; i++) {
                  transform.reinforceInfo.reinforce[i] = props.forget.data["增幅四维"][i]
                }
              }
              if (props.forget.data["强化四维"] && props.forget.data["强化四维"].length > 0) {
                for (var i = 0; i < props.forget.data["强化四维"].length; i++) {
                  transform.reinforceInfo.strengthen[i] = props.forget.data["强化四维"][i]
                }
              }
              if (props.forget.data["强化攻击力"] && props.forget.data["强化攻击力"].length > 0) {
                for (var i = 0; i < props.forget.data["强化攻击力"].length; i++) {
                  transform.reinforceInfo.strengthen[i + 4] = props.forget.data["强化攻击力"][i]
                }
              }
            }
            // 处理强化锻造数据
            transform.reinforceInfo.refine = [0, 0, 0, 0, 0, 0, 0]
            transform.reinforceInfo.refineSW = 0
            if (transform.refine > 0) {
              let dz = props.forget.data["锻造加成"]
              if (dz && dz.length > 0) {
                transform.reinforceInfo.refine[6] = dz[0]
              }
              if (dz && dz.length > 1) {
                transform.reinforceInfo.refineSW = dz[1]
                // transform.reinforceInfo.refine[0] = dz[1];
                // transform.reinforceInfo.refine[1] = dz[1];
                // transform.reinforceInfo.refine[2] = dz[1];
                // transform.reinforceInfo.refine[3] = dz[1];
              }
            }
          }
        }

        // console.log(transform)
      }

      const iconBages = computed(() => {
        let x = transform.badges && transform.badges.length > 0 ? { color: [transform.badges[0]?.type, transform.badges[1]?.type], num: transform.badges.length } : null
        // console.log(x)
        return x
      })

      return () => {
        if (!equip.value) {
          return <div></div>
        }

        return (
          <div class={["approved-form"].concat([props.colums ? "with-colums" : ""].concat("!w-300px"))}>
            <div class="epic title" style="display: flex">
              <eq-icon eq={equip.value} badges={iconBages.value}></eq-icon>
              <div class="eq-name" style="margin-left: 8px">
                <span style="display: flex" class={rarityClass(equip.value.rarity)}>
                  {transform.reinforce > 0 ? <span style="margin-right: 4px">+{transform.reinforce}</span> : <span></span>}
                  {transform.refine > 0 ? <span>({transform.refine})</span> : <span></span>}
                  <span>{equip.value.name}</span>
                </span>
              </div>
              <div class="flex-1 eq-name yellow" style="text-align: right">
                <p style="display: flex">
                  <span style="width: 100%">{equip.value.position}</span>
                </p>
              </div>
            </div>
            {transform.badges && transform.badges.length > 0 ? (
              <div>
                <div class="hr"></div>
                <div style="display: flex">
                  {renderList(transform.badges, (bs, i) => (
                    <div style={i > 0 ? "margin-left: 20px" : ""}>
                      <div class={badgeClass[bs.type]}>[{badgeNames[bs.type]}]</div>
                      {renderList(bs.props, b => (
                        <div>{b}</div>
                      ))}
                    </div>
                  ))}
                </div>
              </div>
            ) : (
              <div></div>
            )}
            <div class="hr"></div>
            {
              //   !props.simple && (
              //   <div>
              //     <div class="hr"></div>
              //     <div class="fame">
              //       <img src="images/common/fame.png" />
              //       冒险家名望 {equip.value.fame}
              //     </div>
              //     <div class="hr"></div>
            }
            {transform.reinforce > 0 || transform.refine > 0 ? (
              <span>
                {transform.reinforce > 0 ? (
                  <span style="margin-right: 5px">
                    {transform.type == 1 ? (
                      <span>
                        <span class="advanced">+{transform.reinforce} 强化</span>/<span class="artifact">增幅</span>
                      </span>
                    ) : (
                      <span class="advanced">+{transform.reinforce} 强化</span>
                    )}
                  </span>
                ) : (
                  <span></span>
                )}
                {transform.refine > 0 ? (
                  <span style="margin-right: 5px" class="rare">
                    +{transform.refine} 锻造
                  </span>
                ) : (
                  <span></span>
                )}
                <span>性能适用</span>
              </span>
            ) : (
              <span></span>
            )}
            {equip.value.prop.base.map(renderStatus(undefined, undefined, true))}
            <div class="hr"></div>
            <div class="green"> &lt;附魔&gt; </div>
            {transform.enchanting != null && transform.enchanting.length > 0 ? (
              <div class="enchanting" style="margin-top:6px">
                {renderList(transform.enchanting, e => (
                  <div>{e.replace("(", " +").replace(")", "")}</div>
                ))}
              </div>
            ) : (
              <div class="gey">未赋予魔法能力</div>
            )}
            {equip.value.prop.effect && equip.value.prop.effect.length > 0 && (
              <div>
                <div class="hr"></div>
                {equip.value.prop.effect.map(renderStatus(effectClass))}
              </div>
            )}
            {transform.reinforceInfo.refineSW > 0 ? (
              <div>
                <div class="hr"></div>
                <div class="green"> &lt;辅助职业专属属性&gt; </div>
                <div class="rare">力量/智力/体力/精神 +{transform.reinforceInfo.refineSW}</div>
              </div>
            ) : (
              <span></span>
            )}

            {(sum_attack.value > 0 || sum_buffer.value > 0 || (props.pps != null && props.pps.length > 0)) && (
              <div>
                <div class="hr"></div>
                <div class="green"> &lt;成长属性&gt; </div>
                {!props.simple && <div>{is_buffer.value ? <div>成长属性总Buff量 {sum_buffer.value}</div> : <div class="text-hex-8a6f36">成长属性总攻击强化 {sum_attack.value}</div>}</div>}
              </div>
            )}
            {props.pps != null && props.pps.length > 0
              ? renderList(props.pps, (x: any, i: number) => (
                  <div style="padding-top: 5px">
                    <div class="yellow">
                      属性 {i + 1} - Lv{transform.growthLvs[i]}
                    </div>
                    {renderList(x.props, p => (
                      <div class="strong paddleft">{p}</div>
                    ))}
                  </div>
                ))
              : renderList(equip.value.prop.growthProps, (p, i: number) => (
                  <div style="padding-bottom: 5px">
                    {p.props && p.props.length > 0 ? (
                      <>
                        <div class="yellow">
                          <span>
                            属性 {i + 1} - Lv{transform.growthLvs[i] || 1}
                          </span>
                        </div>
                        {is_buffer.value ? (
                          <div class="text-hex-8a6f36  paddleft">
                            <span style="margin-right: 10px;">Buff量</span>
                            <span>{transform.growthBuffers[i] || p.buffer}</span>
                          </div>
                        ) : (
                          <div class="text-hex-8a6f36 paddleft">
                            <span style="margin-right: 10px;">攻击强化</span>
                            <span>{transform.growthAttacks[i] || p.attack}</span>
                          </div>
                        )}

                        {renderList(p.props, s => (
                          <div class="strong paddleft">
                            <span>{s}</span>
                          </div>
                        ))}
                      </>
                    ) : (
                      <div class="paddleft suiji-props gey">
                        <span>随机属性</span>
                      </div>
                    )}
                  </div>
                ))}
            {
              // 随机属性装备
            }
            {
              // <div class="bottom">
              //   {slots.default ? (
              //     slots.default()
              //   ) : (
              //     <>
              //       <div class="hr"></div>
              //       <div
              //         class="red"
              //         style="text-align: center; padding-right: 15px"
              //       >
              //         {" "}
              //         合成[x]{" "}
              //       </div>
              //     </>
              //   )}
              // </div>
            }
          </div>
        )
      }
    }
  })
</script>
<style src="./eq-info.scss" scoped></style>
