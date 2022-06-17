<script lang="tsx">
  import { useBasicInfoStore, useCharacterStore } from "@/store"
  import { asyncComputed } from "@vueuse/core"
  import { computed, defineComponent, renderList } from "vue"

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
      const basicStore = useBasicInfoStore()

      const equip = asyncComputed(async () => {
        if (props.eid != undefined) {
          let temp = basicStore.get_equipment_detail(props.eid)
          return temp
        }
      })

      // console.log(equip.value)

      function renderStatus(rowClass?: classNames, spanClass?: classNames) {
        return ({ id, label, num, isRate }: Status) => {
          const array: JSX.Element[] = []

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
          return <div class={[rowClassNames]}>{array}</div>
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

      const characterStore = useCharacterStore()

      const is_buffer = computed(() => characterStore.is_buffer)

      const sum_buffer = computed(() => {
        let s = 0
        if (equip.value?.prop.growthProps && equip.value.prop.growthProps.length > 0) {
          let a = equip.value.prop.growthProps
          for (let item of a) {
            s += item.buffer ?? 0
          }
        }
        return s
      })

      const sum_attack = computed(() => {
        let s = 0
        if (equip.value?.prop.growthProps && equip.value.prop.growthProps.length > 0) {
          let a = equip.value.prop.growthProps
          for (let item of a) {
            s += item.attack
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

      return () => {
        if (!equip.value) {
          return <div></div>
        }

        return (
          <div class={["approved-form"].concat([props.colums ? "with-colums" : ""].concat("!w-300px"))}>
            <div class="epic title" style="display: flex">
              <eq-icon eq={equip.value}></eq-icon>
              <div class="eq-name" style="margin-left: 8px">
                <span style="display: flex" class={rarityClass(equip.value.rarity)}>
                  {equip.value.name}
                </span>
              </div>
              <div class="flex-1 eq-name yellow" style="text-align: right">
                <p style="display: flex">
                  <span style="width: 100%">{equip.value.position}</span>
                </p>
              </div>
            </div>
            <div class="hr"></div>
            <div>
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

              {equip.value.prop.base.map(renderStatus())}
              <div class="hr"></div>
              <div class="green"> &lt;附魔属性&gt; </div>
              <div class="gey">没有附魔属性</div>
            </div>

            {equip.value.prop.effect && equip.value.prop.effect.length > 0 && (
              <div>
                <div class="hr"></div>
                {equip.value.prop.effect.map(renderStatus(effectClass))}
              </div>
            )}
            {
              //   !props.simple && equip.value.prop.bufferProps && equip.value.prop.bufferProps.length > 0 ? (
              //   <div>
              //     <div class="hr"></div>
              //     <div class="green"> &lt;辅助职业专属属性&gt; </div>
              //     {equip.value.prop.bufferProps.map(renderStatus(undefined, effectClass))}
              //   </div>
              // ) : (
              //   <div></div>
              // )
            }
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
                        {is_buffer.value ? (
                          <div class="text-hex-8a6f36  paddleft">
                            <span style="margin-right: 10px;">Buff量</span>
                            <span>{p.buffer}</span>
                          </div>
                        ) : (
                          <div class="text-hex-8a6f36 paddleft">
                            <span style="margin-right: 10px;">攻击强化</span>
                            <span>{p.attack}</span>
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
