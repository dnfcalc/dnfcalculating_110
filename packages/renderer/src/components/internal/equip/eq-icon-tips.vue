<script lang="tsx">
  import {
    defineComponent,
    reactive,
    ref,
    watch,
    computed,
    Teleport
  } from "vue"
  import EqInfo from "./eq-info.vue"
  import EqIcon from "./eq-icon.vue"
  import { debounce } from "lodash"

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
      }
    },
    setup(props, { emit }) {
      const TipsEq = ref({ x: 0, y: 0, show: false })

      let showTipsD = debounce(showEqTips, 1000)

      function showEqTips(e: any) {
        TipsEq.value.show = true
        TipsEq.value.x =
          window.innerWidth - e.clientX > 500
            ? e.clientX + 20
            : e.clientX - 20 - 310
        var dom = document.getElementById("eq-info-tips")
        if (dom != null) {
          TipsEq.value.y =
            window.innerHeight - e.clientY > dom.offsetHeight + 50
              ? e.clientY
              : window.innerHeight - (dom.offsetHeight + 50)
        } else {
          TipsEq.value.y = e.clientY
        }
      }

      function removeEqTips() {
        showTipsD.cancel()
        TipsEq.value.show = false
      }

      function onclick() {
        emit("select", props.eq)
      }

      return () => {
        return (
          <div class="eq-item-icon">
            <eq-icon
              eq={props.eq}
              canClick={props.canClick}
              onclick={onclick}
              onmousemove={showTipsD}
              onmouseout={removeEqTips}
            ></eq-icon>
            <teleport to="body">
              {props.eq && props.showTips && TipsEq.value.show ? (
                <div
                  id="eq-info-tips"
                  class={["eq-info-tips"].concat(
                    props.colums ? "" : "width-no-colums"
                  )}
                  style={
                    "left:" +
                    TipsEq.value.x +
                    "px; top:" +
                    TipsEq.value.y +
                    "px"
                  }
                >
                  <eq-info
                    colums={props.colums}
                    eid={props.eq.id}
                    pps={props.eq.groupId == 10 ? props.eq.props : null}
                  ></eq-info>
                </div>
              ) : (
                <div></div>
              )}
            </teleport>
          </div>
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
    border: 1px solid #1a1a1a;
    background-color: rgba($color: #000000, $alpha: 0.5);
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
