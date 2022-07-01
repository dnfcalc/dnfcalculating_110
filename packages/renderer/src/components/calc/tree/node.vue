<script lang="tsx">
  import { NItem } from "@/components/base"
  import { computed, defineComponent, PropType, ref, renderList, Transition } from "vue"
  import { TreeNode } from "./types"

  const NTreeNode = defineComponent({
    props: {
      label: {
        type: String,
        default: ""
      },
      value: {
        type: [String, Number, Boolean, Object, Array] as PropType<any>,
        default: () => null
      },
      children: {
        type: Array as PropType<TreeNode[]>,
        default: () => []
      },
      depth: {
        type: [String, Number] as PropType<number>,
        default: 0
      },
      depthStyle: {
        type: Function as PropType<(depth: number) => string>
      }
    },
    setup(props, { emit }) {
      const isOpen = ref(false)

      function open() {
        isOpen.value = !isOpen.value
        onSelect(props)
      }

      function onSelect(item: TreeNode) {
        return emit("select", item)
      }

      const depthStyle = computed(() => {
        if (props.depthStyle) {
          return props.depthStyle(props.depth)
        }
        return `padding-left: ${props.depth}rem`
      })

      return () => (
        <div class="w-full i-tree-item">
          <NItem value={props.value} style={depthStyle.value} class="i-tree-item-label" onClick={open}>
            {props.label}
          </NItem>
          <Transition name="dropdown" mode="out-in">
            <div v-show={isOpen.value}>
              {renderList(props.children, item => {
                return <NTreeNode onSelect={onSelect} {...item} depth={Number(props.depth) + 1} />
              })}
            </div>
          </Transition>
        </div>
      )
    }
  })

  export default NTreeNode
</script>
<style>
  .i-tree-item {
    display: flex;
    flex-direction: column;
    cursor: pointer;
  }

  .i-tree-item-label {
    flex: 1;
    padding-left: 0.5rem;
    color: #ddc593;
  }

  .i-tree-dropdown {
    width: 100%;
    max-height: 0;
    overflow: hidden;
    background-color: #fff;
    border-radius: 0.5rem;
    box-shadow: 0 0 0.5rem 0 rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
  }

  .dropdown-active {
    animation: dropdown-enter 0.2s ease-in;
  }

  .dropdown-active {
    animation: dropdown-leave 0.2s ease-in;
  }

  .dropdown-enter-active {
    animation: dropdown-enter 0.2s ease-in;
  }

  .dropdown-leave-active {
    animation: dropdown-leave 0.2s ease-in;
  }

  .dropdown-enter-active {
    animation: dropdown-enter 0.2s ease-in;
  }

  .dropdown-leave-active {
    animation: dropdown-leave 0.2s ease-in;
  }
</style>
