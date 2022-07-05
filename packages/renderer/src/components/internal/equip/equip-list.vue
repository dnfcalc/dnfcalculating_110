<script lang="tsx">
  import { IEquipmentInfo } from "@/api/info/type"
  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
  import { computed, defineComponent, PropType, reactive, renderList, renderSlot, watch } from "vue"

  export default defineComponent({
    props: {
      // 展示列表
      list: {
        type: Array as PropType<IEquipmentInfo[]>,
        default: () => []
      },
      // 按钮名称
      title: {
        type: String,
        default: ""
      },
      // 选中列表
      selected: {
        type: Array as PropType<ID[]>,
        default: () => []
      },
      // 需要高亮的
      highlight: {
        type: Array as PropType<ID[]>,
        default: () => []
      },
      // 是不是有筛选
      showHighlight: {
        type: Boolean,
        default: false
      },
      showTips: {
        type: Boolean,
        default: true
      }
    },
    components: { EquipTips },

    setup(props, { emit, slots }) {
      const selected = reactive<ID[]>(props.selected)
      const highlight = reactive<ID[]>(props.highlight)

      watch(props.selected, () => {
        selected.splice(0, selected.length, ...props.selected)
      })

      // const isSelectAll = computed(() => {
      //   const len = props.highlight.length || props.list.length
      //   return selected.length === len
      // })

      const highlightSelectdCount = computed(() => {
        return selected.filter(item => props.highlight.indexOf(item) >= 0).length
      })

      function selectAll() {
        const new_arr = props.showHighlight
          ? highlightSelectdCount.value > props.highlight.length / 2
            ? selected.filter(item => props.highlight.indexOf(item) < 0)
            : Array.from([...selected, ...props.highlight])
          : selected.length > props.list.length / 2
          ? []
          : props.list.map(item => item.id)
        selected.splice(0, selected.length, ...new_arr)
        props.showHighlight ?? emit("update:highlight", [])
        emit("update:selected", selected)
      }

      function changeState(id: ID) {
        return () => {
          if (selected.includes(id)) {
            selected.splice(selected.indexOf(id), 1)
          } else {
            selected.push(id)
          }
          emit("update:selected", selected)
        }
      }

      return () => {
        return (
          <div>
            <div class="flex mb-1 w-full items-center">
              {renderSlot(slots, "header")}
              <calc-button class="flex-1" onClick={selectAll}>
                {props.title}
              </calc-button>
            </div>
            <div class="flex flex-wrap w-full">
              {renderList(props.list, equ => (
                <EquipTips
                  class="item"
                  eq={equ}
                  canClick={true}
                  showTips={props.showTips}
                  active={selected.includes(equ.id)}
                  hightlight={props.highlight.includes(equ.id)}
                  onUpdate:active={changeState(equ.id)}
                ></EquipTips>
              ))}
            </div>
          </div>
        )
      }
    }
  })
</script>
