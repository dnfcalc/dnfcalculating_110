<script lang="tsx">
  /**
   * @Author: Kritsu
   * @Date:   2021/11/16 18:33:00
   * @Last Modified by:   Kritsu
   * @Last Modified time: 2021/11/17 18:49:21
   */
  import { defineComponent, h, renderSlot } from "vue"
  import NItem from "@/components/base/item"
  import { itemProps } from "@/components/hooks/selection/item"

  export default defineComponent({
    name: "calc-tab",
    props: {
      ...itemProps
    },
    components: { NItem },
    setup(props, { slots }) {
      return () => {
        return <n-item {...props}>{renderSlot(slots, "default")}</n-item>
      }
    }
  })
</script>
