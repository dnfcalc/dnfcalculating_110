<script lang="tsx">
  import {
    computed,
    defineComponent,
    reactive,
    ref,
    renderSlot,
    watch,
    onMounted,
    renderList
  } from "vue"
  import { asyncComputed } from "@vueuse/core"

  import EqIcon from "./eq-icon.vue"

  interface Status {
    id: number
    label: string
    num: number
    isRate: boolean
    info: string
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
      pps: {
        type: Array,
        default: () => []
      }
    },
    setup(props, { emit, slots }) {
      const equip = asyncComputed(async () => {
        if (props.eid) {
          let eq = {
            groupId: 1,
            tips: "技能定制武器",
            position: "太刀(鬼剑士(男))",
            lv: 105,
            naijiu: 48,
            trade: "无法交易",
            price: 0,
            fame: 748,
            prop: {
              base: [
                {
                  id: 1,
                  index: null,
                  label: "物理攻击力",
                  num: 1222,
                  info: null,
                  isRate: false
                },
                {
                  id: 2,
                  index: null,
                  label: "魔法攻击力",
                  num: 1351,
                  info: null,
                  isRate: false
                },
                {
                  id: 3,
                  index: null,
                  label: "独立攻击力",
                  num: 818,
                  info: null,
                  isRate: false
                },
                {
                  id: 6,
                  index: null,
                  label: "力量",
                  num: 85,
                  info: null,
                  isRate: false
                },
                {
                  id: 7,
                  index: null,
                  label: "智力",
                  num: 128,
                  info: null,
                  isRate: false
                }
              ],
              effect: [
                {
                  id: 11,
                  index: null,
                  label: "物理百分比技能",
                  num: null,
                  info: "MP-5% 冷却时间-5%",
                  isRate: false
                },
                {
                  id: 12,
                  index: null,
                  label: "魔法百分比技能",
                  num: null,
                  info: "MP+5% 冷却时间-5%",
                  isRate: false
                },
                {
                  id: 14,
                  index: null,
                  label: "攻击速度",
                  num: 0.08,
                  info: null,
                  isRate: true
                },
                {
                  id: 15,
                  index: null,
                  label: "施放速度",
                  num: 0.05,
                  info: null,
                  isRate: true
                },
                {
                  id: 17,
                  index: null,
                  label: "物理暴击率",
                  num: 0.02,
                  info: null,
                  isRate: true
                },
                {
                  id: 22,
                  index: null,
                  label: "技能攻击力",
                  num: 0.5,
                  info: null,
                  isRate: true
                }
              ],
              growthProps: [
                {
                  id: 21,
                  fromType: null,
                  index: 1,
                  buffer: null,
                  attack: 2223,
                  level: null,
                  type: null,
                  propsStr:
                    "[杀意波动]技能波动领域范围+20%<br>[邪光波动阵]技能波动攻击范围+25%",
                  props: [
                    "[杀意波动]技能波动领域范围+20%",
                    "[邪光波动阵]技能波动攻击范围+25%"
                  ]
                },
                {
                  id: 22,
                  fromType: null,
                  index: 2,
                  buffer: null,
                  attack: 2223,
                  level: null,
                  type: null,
                  propsStr:
                    "施放特定技能时吸收雷神之力，使[邪光波动阵]获得强化，施放[邪光波动阵]时可无施放动作使用<br>- 爆炎波动剑<br>- 不动冥王阵<br>- 天雷波动剑",
                  props: [
                    "施放特定技能时吸收雷神之力，使[邪光波动阵]获得强化，施放[邪光波动阵]时可无施放动作使用",
                    "- 爆炎波动剑",
                    "- 不动冥王阵",
                    "- 天雷波动剑"
                  ]
                },
                {
                  id: 23,
                  fromType: null,
                  index: 3,
                  buffer: null,
                  attack: 2223,
                  level: null,
                  type: null,
                  propsStr:
                    "[爆炎波动剑]爆发间隔距离-90%，爆发位置更变，爆发间隔时间-30%",
                  props: [
                    "[爆炎波动剑]爆发间隔距离-90%，爆发位置更变，爆发间隔时间-30%"
                  ]
                },
                {
                  id: 24,
                  fromType: null,
                  index: 4,
                  buffer: null,
                  attack: 2223,
                  level: null,
                  type: null,
                  propsStr:
                    "[爆炎波动剑]第二次爆发大小+45%<br>[爆炎波动剑]第三次爆发大小+70%",
                  props: [
                    "[爆炎波动剑]第二次爆发大小+45%",
                    "[爆炎波动剑]第三次爆发大小+70%"
                  ]
                }
              ],
              bufferProps: []
            },
            id: 422,
            rarity: "史诗",
            name: "决战之太刀 - 阿修罗",
            icon: "/arms/swordman/katana/218.png",
            group: null,
            rarityClass: "epic"
          }
          return eq
        }
      })

      function renderStatus(rowClass?: classNames, spanClass?: classNames) {
        return ({ id, label, num, isRate }: Status) => {
          const array: JSX.Element[] = []

          array.push(
            <span style={num ? "margin-right: 10px" : undefined}>{label}</span>
          )
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
          return <div class={rowClassNames}>{array}</div>
        }
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

      const growthSpanClass = function (id: number) {
        if (id == 101) {
          return "white"
        }
      }

      const sumFZL = computed(() => {
        let s = 0
        if (
          equip.value?.prop.growthProps &&
          equip.value.prop.growthProps.length > 0
        ) {
          let a = equip.value.prop.growthProps
          for (let item of a) {
            s += item.buffer ?? 0
          }
        }
        return s
      })
      const sumSHZJ = computed(() => {
        let s = 0
        if (
          equip.value?.prop.growthProps &&
          equip.value.prop.growthProps.length > 0
        ) {
          let a = equip.value.prop.growthProps
          for (let item of a) {
            s += item.attack
          }
        }
        return s
      })

      function star() {
        emit("star")
      }

      return () => {
        if (!equip.value) {
          return <div></div>
        }

        return (
          <div
            class={["approved-form"].concat([
              props.colums ? "with-colums" : ""
            ])}
          >
            <div class="epic title" style="display: flex">
              <eq-icon eq={equip.value}></eq-icon>
              <div class="eq-name" style="margin-left: 8px">
                <p style="display: flex">
                  <span style="width: 100%" class={equip.value.rarityClass}>
                    {equip.value.name}
                  </span>
                  {props.star == true ? (
                    <div class="icon-star" onClick={star}>
                      <el-icon class={[props.isStar ? "is-star" : ""]}>
                        <icon-star v-show={!props.isStar} />
                        <icon-star-filled v-show={props.isStar} />
                      </el-icon>
                    </div>
                  ) : (
                    <span></span>
                  )}
                </p>
              </div>
            </div>
            <div class="">
              <div class="hr"></div>
              <span class="strong">
                <span style="color: #f3e500">最上级</span> (100%)
              </span>
              <span class={equip.value.rarityClass} style="float: right">
                {equip.value.rarity}
              </span>
            </div>
            <div class="" style="text-align: right">
              Lv{equip.value.lv}以上可以使用
            </div>
            <div class="red" style="text-align: right">
              {equip.value.trade}
            </div>
            <div class="yellow" style="text-align: right">
              {equip.value.position}
            </div>
            {!props.simple && equip.value.naijiu > 0 && (
              <div>
                耐久度 {equip.value.naijiu}/{equip.value.naijiu}
              </div>
            )}
            {!props.simple && (
              <div>
                <div class="hr"></div>
                <div class="fame">
                  <img src="https://www.tianyongxian.com/dnfstatic/images/icons/base/mingwang.png" />
                  冒险家名望 {equip.value.fame}
                </div>
                <div class="hr"></div>
                {equip.value.prop.base.map(renderStatus())}
                <div class="hr"></div>
                <div class="green"> &lt;附魔属性&gt; </div>
                <div class="gey">没有附魔属性</div>
                <div class="gey">(可以在百科辞典中查看附魔属性)</div>
              </div>
            )}
            {equip.value.prop.effect && equip.value.prop.effect.length > 0 && (
              <div>
                <div class="hr"></div>
                {equip.value.prop.effect.map(renderStatus(effectClass))}
              </div>
            )}
            {!props.simple &&
            equip.value.prop.bufferProps &&
            equip.value.prop.bufferProps.length > 0 ? (
              <div>
                <div class="hr"></div>
                <div class="green"> &lt;辅助职业专属属性&gt; </div>
                {equip.value.prop.bufferProps.map(renderStatus(effectClass))}
              </div>
            ) : (
              <div></div>
            )}
            {(sumSHZJ.value > 0 ||
              (props.pps != null && props.pps.length > 0)) && (
              <div>
                <div class="hr"></div>
                <div class="green"> &lt;成长属性&gt; </div>
                {!props.simple && sumSHZJ.value > 0 && (
                  <div>
                    <div>成长属性总伤害增加 {sumSHZJ.value}</div>
                    {sumFZL.value > 0 && (
                      <div>成长属性总Buff量 {sumFZL.value}</div>
                    )}
                  </div>
                )}
              </div>
            )}
            {props.pps != null && props.pps.length > 0
              ? renderList(props.pps, (x, i: number) => (
                  <div style="padding-top: 5px">
                    <div class="yellow">
                      属性 {i + 1} - {x.typeName}
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
                          <span>属性{i + 1} - Lv1 (EXP 0.00%)</span>
                        </div>
                        <div class="paddleft">
                          <span style="margin-right: 10px;">伤害增加</span>
                          <span>{p.attack}</span>
                        </div>
                        {p.buffer > 0 ? (
                          <div class="paddleft">
                            <span style="margin-right: 10px;">Buff量</span>
                            <span>{p.buffer}</span>
                          </div>
                        ) : (
                          <div></div>
                        )}
                        {renderList(p.props, s => (
                          <div class="strong paddleft">
                            <span>{s}</span>
                          </div>
                        ))}
                      </>
                    ) : (
                      <div class="paddleft suiji-props gey">
                        <span>随机属性, 获取装备后在背包中查看</span>
                      </div>
                    )}
                  </div>
                ))}
            {
              // 随机属性装备
            }
            <div class="bottom">
              {slots.default ? (
                slots.default()
              ) : (
                <>
                  <div class="hr"></div>
                  <div
                    class="red"
                    style="text-align: center; padding-right: 15px"
                  >
                    {" "}
                    合成[x]{" "}
                  </div>
                </>
              )}
            </div>
          </div>
        )
      }
    }
  })
</script>
<style src="./eq-info.scss" scoped></style>
