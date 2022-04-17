<script lang="tsx">
    import { useVModel } from "@vueuse/core"
    import { defineComponent, PropType, ref, renderList, renderSlot } from "vue"
    import { TreeNode } from "./types"
    import { labelPropType, valuePropType } from "@/components/hooks/types"
    import NTreeNode from "./node.vue"
    import NSelection from "@/components/base/selection"

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
                type: Number,
                default: 0
            }
        },
        setup(props, { slots }) {
            const modelValue = useVModel(props, "modelValue")

            return () => {
                return (
                    <NSelection activeClass="i-tree-node-active" v-model={modelValue.value} class="i-tree">
                        {renderList(props.data, item => {
                            return <NTreeNode {...item} depth={props.depth} />
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
