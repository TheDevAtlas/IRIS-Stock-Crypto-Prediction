using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CandlestickChart : MonoBehaviour
{
    public float chartWidth = 10f;
    public float chartHeight = 5f;
    public float candleWidth = 0.5f;
    public int numCandle = 0;
    public Sprite candleSprite;

    void Start()
    {
        CreateCandlestick(150f, 170f, 180f, 140f, (candleWidth + 0.15f) * (float)numCandle);  // Example call for a single candlestick
        numCandle++;
        CreateCandlestick(160f, 155f, 170f, 150f, (candleWidth + 0.15f) * (float)numCandle);  // Example call for another candlestick
    }

    void CreateCandlestick(float openPrice, float closePrice, float highPrice, float lowPrice, float num)
    {
        float minPrice = Mathf.Min(openPrice, closePrice, highPrice, lowPrice);
        float maxPrice = Mathf.Max(openPrice, closePrice, highPrice, lowPrice);
        float priceRange = maxPrice - minPrice;
        float verticalScale = chartHeight / priceRange;

        GameObject candlestick = new GameObject("Candlestick");
        candlestick.transform.SetParent(transform);

        candlestick.transform.localPosition = new Vector3(chartWidth / 2f + num, (openPrice - minPrice) * verticalScale / 2f, 0f);
        candlestick.transform.localScale = new Vector3(candleWidth, (closePrice - openPrice) * verticalScale, 1f);

        SpriteRenderer spriteRenderer = candlestick.AddComponent<SpriteRenderer>();
        spriteRenderer.sprite = candleSprite;
        spriteRenderer.color = (closePrice > openPrice) ? Color.green : Color.red;

        LineRenderer lineRenderer = candlestick.AddComponent<LineRenderer>();
        lineRenderer.positionCount = 2;
        lineRenderer.startWidth = 0.02f;
        lineRenderer.endWidth = 0.02f;
        lineRenderer.SetPosition(0, new Vector3(chartWidth / 2f + num, (highPrice - minPrice) * verticalScale / 2f, 0f));
        lineRenderer.SetPosition(1, new Vector3(chartWidth / 2f + num, (lowPrice - minPrice) * verticalScale / 2f, 0f));
        lineRenderer.material = new Material(Shader.Find("Sprites/Default"));
        lineRenderer.startColor = (closePrice > openPrice) ? Color.green : Color.red;
        lineRenderer.endColor = (closePrice > openPrice) ? Color.green : Color.red;
    }
}
