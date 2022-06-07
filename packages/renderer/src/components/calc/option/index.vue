<script lang="tsx">
  import { defineComponent, renderSlot } from "vue"
  import { itemProps } from "@/components/hooks/selection/item"
  import NItem from "@/components/base/item"
  export default defineComponent({
    props: {
      ...itemProps
    },
    setup(props, { slots }) {
      return () => <NItem {...props}>{renderSlot(slots, "default")}</NItem>
    }
  })
</script>
