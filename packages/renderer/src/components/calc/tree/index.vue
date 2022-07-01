<script lang="tsx">
  import NSelection from "@/components/base/selection"
  import { labelPropType, valuePropType } from "@/components/hooks/types"
  import { useVModel } from "@vueuse/core"
  import { defineComponent, PropType, renderList } from "vue"
  import CalcTreeNode from "./node.vue"
  import { TreeNode } from "./types"

  const Tree = defineComponent({
    name: "calc-tree",
    props: {
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
      }

      return () => {
        return (
          <NSelection activeClass="i-tree-node-active" v-model={modelValue.value} class="i-tree">
            {renderList(props.data, item => {
              return <CalcTreeNode onSelect={onSelect} depth-style={props.depthStyle} {...item} depth={props.depth} />
            })}
          </NSelection>
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

  .i-tree-node-active {
    color: red;
    border: 1px solid;
  }
</style>
