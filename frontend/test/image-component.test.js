import { mount } from '@vue/test-utils'
import ImageComponent from '../src/components/ImageComponent.vue';

test('mount component', async () => {
    expect(ImageComponent).toBeTruthy()

    const wrapper = mount(ImageComponent, {
        props: {
            value: 0.5
        }
    });

    expect(wrapper.isVisible()).toBe(true);
})