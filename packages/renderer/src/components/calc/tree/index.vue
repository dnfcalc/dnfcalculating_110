<script lang="tsx">
  import { listProps } from "@/components/hooks/selection/list"
  import { labelPropType, valuePropType } from "@/components/hooks/types"
  import { useVModel } from "@vueuse/core"
  import { defineComponent, PropType, renderList } from "vue"
  import CalcTreeNode from "./node.vue"
  import { TreeNode } from "./types"

  const Tree = defineComponent({
    name: "calc-tree",
    props: {
      ...listProps,
      modelValue: {
        type: valuePropType,
        default: () => null
      },
      idKey: {
        type: String,
        default: "id"
      },
      label: {
        type: labelPropType
      },
      data: {
        type: Array as PropType<TreeNode[]>,
        default: () => []
      },
      depth: {
        type: [Number, String] as PropType<number>,
        default: () => 0
      },
      depthStyle: {
        type: Function as PropType<(depth: number) => string>
      }
    },
    setup(props, { slots, emit }) {
      const modelValue = useVModel(props, "modelValue")

      function onSelect(item: TreeNode) {
        console.log(item)
        emit("select", item)
        item.onSelect?.()
      }

      return () => {
        return (
          <calc-selection {...props} activeClass="i-tree-node-active" v-model={modelValue.value} class="i-tree">
            {renderList(props.data, item => {
              return <CalcTreeNode {...item} onSelect={onSelect} depth-style={props.depthStyle} depth={props.depth} />
            })}
          </calc-selection>
        )
      }
    }
  })

  export default Tree
</script>
<style>
  .i-tree {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }
</style>
