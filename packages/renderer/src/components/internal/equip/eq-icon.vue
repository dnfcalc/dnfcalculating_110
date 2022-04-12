<script lang="tsx">
  import { defineComponent, reactive, ref } from "vue"

  interface EqIconType {
    rarityClass?: string
    active?: boolean
    icon?: string
    id?: number
  }

  export default defineComponent({
    name: "eq-icon",
    props: {
      eq: {
        type: Object,
        default: () => {}
      },
      showTips: {
        type: Boolean,
        default: false
      },
      active: {
        type: Boolean,
        default: true
      }
    },
    setup(props, { emit }) {
      function onclick() {
        // eq.value.active = !eq.value.active
        emit("change", !props.active)
      }

      return () => {
        return (
          <div onClick={onclick}>
            <div class={props.active ? "" : "floatLayer"}></div>
            <div class="eq-item-box">
              {props.eq && props.eq.icon ? (
                <div
                  class={["eq-icon"].concat([
                    props.eq.rarityClass ?? "epic"
                    // eq.value.active ? '' : 'gray'
                  ])}
                >
                  <img src={"./images/equipment/" + props.eq.icon} />
                </div>
              ) : (
                <span class="icon"></span>
              )}
            </div>
          </div>
        )
      }
    }
  })
</script>
<style scoped lang="scss">
  .eq-item-box {
    width: 30px;
    height: 30px;
    display: inline-block;
  }

  .floatLayer {
    position: absolute;
    width: 30px;
    height: 30px;
    z-index: 2;
    background-color: #00000080;
  }

  .eq-icon {
    width: 30px;
    height: 30px;
    background-image: linear-gradient(#e66465, #000);
    position: relative;
    display: inline-block;

    &.gray {
      -webkit-filter: grayscale(100%);
      -moz-filter: grayscale(100%);
      -ms-filter: grayscale(100%);
      -o-filter: grayscale(100%);
      filter: grayscale(100%);
      filter: gray;
    }

    &::before {
      content: "";
      width: 28px;
      height: 28px;
      display: inline-block;
      position: absolute;
      background-color: rgba($color: #000000, $alpha: 1);
      top: 1px;
      left: 1px;
    }

    &.normal {
      background-image: linear-gradient(#ffffff, #000);
    }
    &.advanced {
      background-image: linear-gradient(#61c8de, #000);
    }
    &.rare {
      background-image: linear-gradient(#a060e4, #000);
    }
    &.artifact {
      background-image: linear-gradient(#ef00ef, #000);
    }
    &.legend {
      background-image: linear-gradient(#e96e00, #000);
    }
    &.epic {
      background-image: linear-gradient(#e7a300, #000);
    }
    &.myth {
      background-image: linear-gradient(#e7a300, #000);
    }

    // &.can-click:hover {
    //   cursor: pointer;
    //   background-image: linear-gradient(#3ae7fa, #3ae7fa);
    // }

    > img {
      position: relative;
      top: 1px;
      left: 1px;
      width: 28px;
      height: 28px;
    }
  }
</style>
