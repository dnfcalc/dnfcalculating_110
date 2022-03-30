<script lang="tsx">
  import {
    defineComponent,
    onMounted,
    reactive,
    ref,
    watch,
    computed
  } from "vue"
  // import useImage from "@/hooks/image"

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
      canClick: {
        type: Boolean,
        default: false
      }
    },
    setup(props, { emit }) {
      // const resolve = useImage("equipment", false)

      function onclick() {
        emit("click", props.eq)
      }

      return () => {
        return (
          <div class="eq-item-box" onClick={onclick}>
            {props.eq && props.eq.icon ? (
              <div
                class={["eq-icon"].concat([
                  props.eq.rarityClass,
                  props.canClick ? "can-click" : ""
                ])}
              >
                <img src="https://www.tianyongxian.com/dnfstatic/images/equipment/arms/swordman/katana/218.png" />
              </div>
            ) : (
              <span class="icon"></span>
            )}
          </div>
        )
      }
    }
  })
</script>
<style scoped lang="scss">
  .eq-item-box {
    width: 38px;
    height: 38px;
    display: inline-block;
  }

  .eq-icon {
    width: 38px;
    height: 38px;
    background-image: linear-gradient(#e66465, #000);
    position: relative;
    display: inline-block;

    &::before {
      content: "";
      width: 36px;
      height: 36px;
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

    &.can-click:hover {
      cursor: pointer;
      background-image: linear-gradient(#3ae7fa, #3ae7fa);
    }

    > img {
      position: relative;
      top: 1px;
      left: 1px;
      width: 36px;
      height: 36px;
    }
  }
</style>
