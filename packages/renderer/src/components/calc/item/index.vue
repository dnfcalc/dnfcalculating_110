<script lang="tsx">
  import { itemProps, useSelectionItem } from "@/components/hooks/selection/item"
  import { defineComponent } from "vue"

  export default defineComponent({
    name: "i-item",
    props: itemProps,
    setup(props, context) {
      const { itemClass, change, render } = useSelectionItem(props, context)

      return () => (
        <div onClick={change} class={itemClass.value}>
          {render()}
        </div>
      )
    }
  })
</script>
