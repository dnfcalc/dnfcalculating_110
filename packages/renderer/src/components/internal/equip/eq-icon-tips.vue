<script lang="tsx">
  import { defineComponent, ref } from "vue"
  import EqInfo from "./eq-info.vue"
  import EqIcon from "./eq-icon.vue"
  import { useVModel } from "@vueuse/core"

  export default defineComponent({
    name: "eq-icon-tips",
    components: { EqInfo, EqIcon },
    props: {
      eq: {
        type: Object,
        default: () => {}
      },
      showTips: {
        type: Boolean,
        default: false
      },
      canClick: {
        type: Boolean,
        default: false
      },
      colums: {
        type: Boolean,
        default: false
      },
      active: {
        type: Boolean,
        default: true
      },
      hightlight: {
        type: Boolean,
        default: false
      },
      forget: {
        type: Object,
        default: () => {}
      },
      pps: {
        type: Array,
        default: () => []
      }
    },
    setup(props, { emit }) {
      function handleClick() {
        emit("select", props.eq)
      }

      const active = useVModel(props, "active")

      function renderEqinfo() {
        return <eq-icon class="eq-item-icon" forget={props.forget} eq={props.eq} canClick={props.canClick} onClick={handleClick} v-model:active={active.value} hightlight={props.hightlight}></eq-icon>
      }

      return () => {
        return props.showTips ? (
          <calc-tooltip lazy>
            {{
              default: renderEqinfo,
              popper() {
                return <eq-info colums={props.colums} forget={props.forget} eid={Number(props.eq.id)} pps={props.pps}></eq-info>
              }
            }}
          </calc-tooltip>
        ) : (
          renderEqinfo()
        )
      }
    }
  })
</script>
<style scoped lang="scss">
  .eq-item-icon {
    position: relative;
    display: inline-block;
    height: 30px;
    width: 30px;
    // border: 1px solid #1a1a1a;
    // background-color: rgba($color: #000000, $alpha: 0.5);
  }

  .eq-info-tips {
    position: fixed;
    z-index: 2147483647;

    &.width-no-colums {
      background-color: rgba($color: #000000, $alpha: 0.92);
      width: 285px;
      border: 1px solid gray;
      text-shadow: #000 1px 0 0, #000 0 1px 0, #000 -1px 0 0, #000 0 -1px 0;
    }
  }
</style>
