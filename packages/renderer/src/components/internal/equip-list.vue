<script lang="tsx">
  import { IEquipmentInfo } from "@/api/info/type"
  import { computed, defineComponent, PropType, reactive, renderList, renderSlot, watch } from "vue"
  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"

  export default defineComponent({
    props: {
      list: {
        type: Array as PropType<IEquipmentInfo[]>,
        default: () => []
      },
      title: {
        type: String,
        default: ""
      },
      selected: {
        type: Array as PropType<number[]>,
        default: () => []
      },
      highlight: {
        type: Array as PropType<number[]>,
        default: () => []
      },
      showHighlight: {
        type: Boolean,
        default: false
      }
    },
    components: { EquipTips },

    setup(props, { emit, slots }) {
      const selected = reactive<number[]>(props.selected)

      watch(props.selected, () => {
        selected.splice(0, selected.length, ...props.selected)
      })

      const isSelectAll = computed(() => {
        const len = props.highlight.length || props.list.length
        return selected.length === len
      })

      function selectAll() {
        const new_arr = isSelectAll.value ? [] : props.showHighlight ? props.highlight : props.list.map(item => item.id)
        selected.splice(0, selected.length, ...new_arr)
        emit("update:selected", selected)
      }

      function changeState(id: number) {
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
            <div class="mb-1 flex items-center w-full">
              {renderSlot(slots, "header")}
              <calc-button class="flex-1" onClick={selectAll}>
                {props.title}
              </calc-button>
            </div>
            <div class="w-full">
              {renderList(props.list, equ => (
                <EquipTips class="item" eq={equ} canClick={true} show-tips active={selected.includes(equ.id)} hightlight={props.highlight.includes(equ.id)} onChange={changeState(equ.id)}></EquipTips>
              ))}
            </div>
          </div>
        )
      }
    }
  })
</script>
